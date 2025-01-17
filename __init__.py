# -*- coding: utf-8 -*-
# Copyright (c) 2017 Benedict Dudel
# Copyright (c) 2023 Max
# Copyright (c) 2023 Pete-Hamlin
#
# Adapted for "Calculate Anything" in the style of the "Pass" plugin script.
# Original "Calculate Anything" by @tchar
#
# This plugin provides currency, units, date/time conversions, base conversions
# and general calculator functionality within Albert.

import os
import sys
from albert import (
    PluginInstance,
    TriggerQueryHandler,
    StandardItem,
    Action,
    runDetachedProcess,
    setClipboardText,
)
import re

# Plugin metadata
md_iid = "2.0"
md_version = "0.1"
md_name = "Calculate Anything"
md_description = (
    "An Albert extension that calculates anything and converts currency, units and time."
)
md_license = "MIT"
md_url = "https://github.com/tchar/ulauncher-albert-calculate-anything"
md_authors = ["@tchar"]
md_lib_dependencies = [
    "Pint",              # Pint package for unit conversion
    "simpleeval",        # Evaluate simple mathematical expressions
    "parsedatetime",     # Parse natural language dates
    "pytz",              # Handle time zones
    "babel",             # Optional, for translations and locale formatting
]


################################### SETTINGS #######################################
# The following defaults can be changed via the plugin's configWidget or by editing
# the below lines directly.

# Currency provider: one of ("internal", "fixerio")
DEFAULT_CURRENCY_PROVIDER = "internal"
# API key (for fixer.io or similar)
DEFAULT_API_KEY = "" #put your fixerio key here
# Cache update interval (defaults to one day = 86400 seconds)
DEFAULT_CACHE = 86400
# Default currencies to show if no target is provided
DEFAULT_CURRENCIES = "USD,EUR,GBP,CAD, BRL"
# Default cities to show when converting timezones
DEFAULT_CITIES = "New York City US, London GB, Madrid ES, Vancouver CA, Athens GR, São Paulo BR"
# Units conversion mode ("normal" or "crazy")
DEFAULT_UNITS_MODE = "normal"
# Show placeholder if query is empty
DEFAULT_SHOW_EMPTY_PLACEHOLDER = True
# Triggers (keywords that activate this extension)
DEFAULT_TRIGGERS = ["=", "time", "dec", "bin", "hex", "oct"]
####################################################################################

try:
    from calculate_anything.constants import MAIN_DIR
except ImportError:
    MAIN_DIR = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(MAIN_DIR)

from calculate_anything import logging
from calculate_anything.preferences import Preferences
from calculate_anything.lang import LanguageService
from calculate_anything.query.handlers import (
    MultiHandler,
    UnitsQueryHandler,
    CalculatorQueryHandler,
    PercentagesQueryHandler,
    TimeQueryHandler,
    Base10QueryHandler,
    Base2QueryHandler,
    Base8QueryHandler,
    Base16QueryHandler,
)
from calculate_anything.utils import images_dir

def initialize_preferences(
    currency_provider: str,
    api_key: str,
    cache_interval: int,
    default_currencies: str,
    default_cities: str,
    units_mode: str
):
    """
    Helper function to set up Calculate Anything preferences and providers.
    """
    preferences = Preferences()
    preferences.language.set("en_US")
    preferences.currency.add_provider(currency_provider.lower(), api_key or "")
    preferences.currency.set_cache_update_frequency(cache_interval)
    preferences.currency.set_default_currencies(default_currencies)
    preferences.units.set_conversion_mode(units_mode)
    preferences.time.set_default_cities(default_cities)
    preferences.commit()

class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        # Initialize plugin
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(
            self,
            self.id,
            self.name,
            self.description,
            synopsis="<expression>",
            # Use the first trigger by default. You can change this to your liking.
            # e.g., if you want the plugin to trigger with "calc ", set defaultTrigger="calc ".
            defaultTrigger=DEFAULT_TRIGGERS[0] + " "
        )

        # Icon used in results
        self.iconUrls = [os.path.join(MAIN_DIR, images_dir("icon.svg"))]

        # Read configuration or use defaults
        self._currencyProvider = self.readConfig("currency_provider", str) or DEFAULT_CURRENCY_PROVIDER
        self._apiKey = self.readConfig("api_key", str) or DEFAULT_API_KEY
        self._cache = self.readConfig("cache", int) or DEFAULT_CACHE
        self._defaultCurrencies = self.readConfig("default_currencies", str) or DEFAULT_CURRENCIES
        self._defaultCities = self.readConfig("default_cities", str) or DEFAULT_CITIES
        self._unitsMode = self.readConfig("units_mode", str) or DEFAULT_UNITS_MODE
        self._showEmptyPlaceholder = (
            self.readConfig("show_empty_placeholder", bool) or DEFAULT_SHOW_EMPTY_PLACEHOLDER
        )

        self._triggerCalculator = self.readConfig("triggerCalculator", str) or "="
        self._triggerTime = self.readConfig("triggerTime", str) or "time"
        self._triggerHex = self.readConfig("triggerHex", str) or "hex"
        self._triggerBinary = self.readConfig("triggerBinary", str) or "bin"
        self._triggerDecimal = self.readConfig("triggerDecimal", str) or "dec"
        self._triggerOctal = self.readConfig("triggerOctal", str) or "oct"

        # Initialize the "Calculate Anything" core preferences
        initialize_preferences(
            self._currencyProvider,
            self._apiKey,
            self._cache,
            self._defaultCurrencies,
            self._defaultCities,
            self._unitsMode
        )

    #
    # Properties allow reading/writing config from a single place
    #
    @property
    def currencyProvider(self) -> str:
        return self._currencyProvider

    @currencyProvider.setter
    def currencyProvider(self, value: str):
        self._currencyProvider = value
        self.writeConfig("currency_provider", value)

    @property
    def apiKey(self) -> str:
        return self._apiKey

    @apiKey.setter
    def apiKey(self, value: str):
        self._apiKey = value
        self.writeConfig("api_key", value)

    @property
    def cache(self) -> int:
        return self._cache

    @cache.setter
    def cache(self, value: int):
        self._cache = value
        self.writeConfig("cache", value)

    @property
    def defaultCurrencies(self) -> str:
        return self._defaultCurrencies

    @defaultCurrencies.setter
    def defaultCurrencies(self, value: str):
        self._defaultCurrencies = value
        self.writeConfig("default_currencies", value)

    @property
    def defaultCities(self) -> str:
        return self._defaultCities

    @defaultCities.setter
    def defaultCities(self, value: str):
        self._defaultCities = value
        self.writeConfig("default_cities", value)

    @property
    def unitsMode(self) -> str:
        return self._unitsMode

    @unitsMode.setter
    def unitsMode(self, value: str):
        self._unitsMode = value
        self.writeConfig("units_mode", value)

    @property
    def showEmptyPlaceholder(self) -> bool:
        return self._showEmptyPlaceholder

    @showEmptyPlaceholder.setter
    def showEmptyPlaceholder(self, value: bool):
        self._showEmptyPlaceholder = value
        self.writeConfig("show_empty_placeholder", value)

    @property
    def triggerCalculator(self):
        return self._triggerCalculator

    @triggerCalculator.setter
    def triggerCalculator(self, value):
        self._triggerCalculator = value.strip()
        self.writeConfig("triggerCalculator", self._triggerCalculator)

    @property
    def triggerTime(self):
        return self._triggerTime

    @triggerTime.setter
    def triggerTime(self, value):
        self._triggerTime = value.strip()
        self.writeConfig("triggerTime", self._triggerTime)

    @property
    def triggerHex(self):
        return self._triggerHex

    @triggerHex.setter
    def triggerHex(self, value):
        self._triggerHex = value.strip()
        self.writeConfig("triggerHex", self._triggerHex)

    @property
    def triggerBinary(self):
        return self._triggerBinary

    @triggerBinary.setter
    def triggerBinary(self, value):
        self._triggerBinary = value.strip()
        self.writeConfig("triggerBinary", self._triggerBinary)

    @property
    def triggerDecimal(self):
        return self._triggerDecimal

    @triggerDecimal.setter
    def triggerDecimal(self, value):
        self._triggerDecimal = value.strip()
        self.writeConfig("triggerDecimal", self._triggerDecimal)

    @property
    def triggerOctal(self):
        return self._triggerOctal

    @triggerOctal.setter
    def triggerOctal(self, value):
        self._triggerOctal = value.strip()
        self.writeConfig("triggerOctal", self._triggerOctal)
    #
    # Provide a config widget so users can modify settings via the Albert UI
    #
    def configWidget(self):
        return [
            {
                "type": "spinbox",
                "property": "cache",
                "label": "Cache Update Interval (seconds)",
                "widget_properties": {"min": 0, "max": 604800},
            },
            {
                "type": "lineedit",
                "property": "currencyProvider",
                "label": "Currency Provider (internal or fixerio)",
            },
            {
                "type": "lineedit",
                "property": "apiKey",
                "label": "API Key (for fixer.io or similar)",
            },
            {
                "type": "lineedit",
                "property": "defaultCurrencies",
                "label": "Default Currencies",
            },
            {
                "type": "lineedit",
                "property": "defaultCities",
                "label": "Default Cities for Timezones",
            },
            {
                "type": "lineedit",
                "property": "unitsMode",
                "label": "Units Conversion Mode (normal or crazy)",
            },
            {
                "type": "checkbox",
                "property": "showEmptyPlaceholder",
                "label": "Show placeholder if no query?",
            },
            {
                "type": "lineedit",
                "property": "triggerCalculator",
                "label": "Calculator Trigger (e.g., '=')",
            },
            {
                "type": "lineedit",
                "property": "triggerTime",
                "label": "Time Conversion Trigger (e.g., 'time')",
            },
            {
                "type": "lineedit",
                "property": "triggerHex",
                "label": "Hexadecimal Conversion Trigger (e.g., 'hex')",
            },
            {
                "type": "lineedit",
                "property": "triggerBinary",
                "label": "Binary Conversion Trigger (e.g., 'bin')",
            },
            {
                "type": "lineedit",
                "property": "triggerDecimal",
                "label": "Decimal Conversion Trigger (e.g., 'dec')",
            },
            {
                "type": "lineedit",
                "property": "triggerOctal",
                "label": "Octal Conversion Trigger (e.g., 'oct')",
            },
        ]

            #
            # The main entry point for queries
            #
    def handleTriggerQuery(self, query):

        # Because we set defaultTrigger to the first item in our triggers list,
        # the user typed something like "= 2+2" or "time 16:00" etc.

        user_input = query.string

        if not user_input and not self.showEmptyPlaceholder:
            return


        results = self.getCalculateAnythingResults(user_input)
        if results:
            query.add(results)


    def getCalculateAnythingResults(self, user_input):
        """
        Return a list of StandardItems based on user_input, applying the logic
        for each specific trigger (calculator, time, base conversions, etc.).
        Defaults to the calculator if no triggers are found or matched.
        """

        calc_pattern = re.compile(r"^\s*[\d\s\+\-\*\/\(\)\.\^\%sqrtlogexp]+$")

        is_calc_input = bool(calc_pattern.match(user_input.strip()))
        if is_calc_input:
            trigger = ""
            query_nokw = user_input.strip()
        else:
            tokens = user_input.split(None, 1)
            trigger = tokens[0].lower() if tokens and tokens[0][0].isalpha() else ""
            query_nokw = user_input.strip() if not trigger else (tokens[1] if len(tokens) > 1 else "")

     
        match trigger:
            case t if t == self.triggerCalculator:
                return self.buildResults(query_nokw, calculator_only=True)
            case t if t == self.triggerTime:
                return self.buildResults(query_nokw, trigger_mode="time")
            case t if t == self.triggerHex:
                return self.buildResults(query_nokw, trigger_mode="hex")
            case t if t == self.triggerBinary:
                return self.buildResults(query_nokw, trigger_mode="bin")
            case t if t == self.triggerDecimal:
                return self.buildResults(query_nokw, trigger_mode="dec")
            case t if t == self.triggerOctal:
                return self.buildResults(query_nokw, trigger_mode="oct")
            case _:
                return self.buildResults(query_nokw, calculator_only=True)




    def buildResults(self, query_string, calculator_only=False, trigger_mode=None):
        """
        Using the logic from the original script, build a list of StandardItems.
        """
        # If we're ignoring triggers, we handle everything with the calculator handlers

        if calculator_only:
            handlers = [UnitsQueryHandler, CalculatorQueryHandler, PercentagesQueryHandler]
            query_str = CalculatorQueryHandler().keyword + " " + query_string
            mode = "calculator"
        else:
            # Dispatch to the relevant handlers based on trigger_mode
            if trigger_mode == "time":
                query_str = TimeQueryHandler().keyword + " " + query_string
                handlers = [TimeQueryHandler]
                mode = "time"
            elif trigger_mode == "dec":
                query_str = Base10QueryHandler().keyword + " " + query_string
                handlers = [Base10QueryHandler]
                mode = "dec"
            elif trigger_mode == "hex":
                query_str = Base16QueryHandler().keyword + " " + query_string
                handlers = [Base16QueryHandler]
                mode = "hex"
            elif trigger_mode == "oct":
                query_str = Base8QueryHandler().keyword + " " + query_string
                handlers = [Base8QueryHandler]
                mode = "oct"
            elif trigger_mode == "bin":
                query_str = Base2QueryHandler().keyword + " " + query_string
                handlers = [Base2QueryHandler]
                mode = "bin"
            else:
                # Default is calculator
                query_str = CalculatorQueryHandler().keyword + " " + query_string
                handlers = [UnitsQueryHandler, CalculatorQueryHandler, PercentagesQueryHandler]
                mode = "calculator"

        # Actually run the MultiHandler for the user input
        mh = MultiHandler()
        results = mh.handle(query_str, *handlers)

        items = []
        for idx, result in enumerate(results):
            icon_path = result.icon or images_dir('icon.svg')
            icon_path = os.path.join(MAIN_DIR, icon_path)

            actions = []
            if result.clipboard is not None:
                actions.append(
                    Action(
                        "clipboard",
                        "Copy to clipboard",
                        lambda c=result.clipboard: setClipboardText(c),
                    )
                )

            items.append(
                StandardItem(
                    id=f"{md_name}_{idx}",
                    text=result.name,
                    subtext=result.description,
                    iconUrls=[icon_path],
                    actions=actions,
                )
            )
            print(f"Added item {idx}: id={md_name}_{idx}, text={result.name}, subtext={result.description}, iconUrls={[icon_path]}, actions={actions}")

        # If no items and we need to show a placeholder, build it
        if not items and (query_string.strip() == "" or self.showEmptyPlaceholder):
            items = self.buildPlaceholder(mode, query_string)

        return items

    def buildPlaceholder(self, mode, query_string):

        """
        Build a "no results" placeholder item, localized if possible.
        """
        icon_path = os.path.join(MAIN_DIR, images_dir("icon.svg"))
        no_result_text = LanguageService().translate("no-result", "misc")
        no_result_sub = LanguageService().translate(f"no-result-{mode}-description", "misc")

        return [
            StandardItem(
                id="calculate_anything_no_result",
                text=no_result_text,
                subtext=no_result_sub,
                iconUrls=[icon_path],
            )
        ]
