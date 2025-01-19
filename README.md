# <img src="calculate_anything/images/icon.svg" alt="drawing" width="25"/> Calculate Anything

[![Platforms](https://img.shields.io/badge/platforms-Linux%20%7C%20Windows%20%7C%20macOS-%23818181)](https://github.com/tchar/ulauncher-albert-calculate-anything/actions)
[![Python Versions](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-%23007ec6?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj4gIDxkZWZzPiAgICA8bGluZWFyR3JhZGllbnQgaWQ9InB5WWVsbG93IiBncmFkaWVudFRyYW5zZm9ybT0icm90YXRlKDQ1KSI+ICAgICAgPHN0b3Agc3RvcC1jb2xvcj0iI2ZlNSIgb2Zmc2V0PSIwLjYiLz4gICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjZGExIiBvZmZzZXQ9IjEiLz4gICAgPC9saW5lYXJHcmFkaWVudD4gICAgPGxpbmVhckdyYWRpZW50IGlkPSJweUJsdWUiIGdyYWRpZW50VHJhbnNmb3JtPSJyb3RhdGUoNDUpIj4gICAgICA8c3RvcCBzdG9wLWNvbG9yPSIjNjlmIiBvZmZzZXQ9IjAuNCIvPiAgICAgIDxzdG9wIHN0b3AtY29sb3I9IiM0NjgiIG9mZnNldD0iMSIvPiAgICA8L2xpbmVhckdyYWRpZW50PiAgPC9kZWZzPiAgPHBhdGggZD0iTTI3LDE2YzAtNyw5LTEzLDI0LTEzYzE1LDAsMjMsNiwyMywxM2wwLDIyYzAsNy01LDEyLTExLDEybC0yNCwwYy04LDAtMTQsNi0xNCwxNWwwLDEwbC05LDBjLTgsMC0xMy05LTEzLTI0YzAtMTQsNS0yMywxMy0yM2wzNSwwbDAtM2wtMjQsMGwwLTlsMCwweiBNODgsNTB2MSIgZmlsbD0idXJsKCNweUJsdWUpIi8+ICA8cGF0aCBkPSJNNzQsODdjMCw3LTgsMTMtMjMsMTNjLTE1LDAtMjQtNi0yNC0xM2wwLTIyYzAtNyw2LTEyLDEyLTEybDI0LDBjOCwwLDE0LTcsMTQtMTVsMC0xMGw5LDBjNywwLDEzLDksMTMsMjNjMCwxNS02LDI0LTEzLDI0bC0zNSwwbDAsM2wyMywwbDAsOWwwLDB6IE0xNDAsNTB2MSIgZmlsbD0idXJsKCNweVllbGxvdykiLz4gIDxjaXJjbGUgcj0iNCIgY3g9IjY0IiBjeT0iODgiIGZpbGw9IiNGRkYiLz4gIDxjaXJjbGUgcj0iNCIgY3g9IjM3IiBjeT0iMTUiIGZpbGw9IiNGRkYiLz48L3N2Zz4=)](https://www.python.org/)
[![License](https://img.shields.io/github/license/tchar/ulauncher-albert-calculate-anything?color=%23007ec6)](LICENSE)
[![Latest Version](https://img.shields.io/github/v/tag/tchar/ulauncher-albert-calculate-anything?label=version)](https://github.com/tchar/ulauncher-albert-calculate-anything/releases)
<!-- [![Requirements Status](https://requires.io/github/tchar/ulauncher-albert-calculate-anything/requirements.svg?branch=master)](https://requires.io/github/tchar/ulauncher-albert-calculate-anything/requirements/?branch=master) -->

[![Linux CI](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-linux.yml/badge.svg)](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-linux.yml)
[![Benchmark](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/benchmark-linux.yml/badge.svg)](https://tchar.github.io/ulauncher-albert-calculate-anything/benchmarks/)
[![CodeQL](https://github.com/tchar/ulauncher-albert-calculate-anything/workflows/CodeQL/badge.svg)](https://github.com/tchar/ulauncher-albert-calculate-anything/security/code-scanning)
[![Codecov](https://codecov.io/gh/tchar/ulauncher-albert-calculate-anything/branch/master/graph/badge.svg?token=FDMWA8UDJW)](https://codecov.io/gh/tchar/ulauncher-albert-calculate-anything)
<!-- [![Windows CI](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-windows.yml/badge.svg)](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-windows.yml) -->
<!-- [![macOS CI](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-macos.yml/badge.svg)](https://github.com/tchar/ulauncher-albert-calculate-anything/actions/workflows/ci-macos.yml) -->

[![Code Style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

[![Benchmarks](https://img.shields.io/badge/Benchmarks-blue)](https://tchar.github.io/ulauncher-albert-calculate-anything/benchmarks/)


`Ulauncher/Albert Calculate Anything` is an extension for [Ulauncher](https://ulauncher.io/) and [Albert](https://github.com/albertlauncher/albert) to calculate things like currency, time, percentage, units, complex equations, base-n expressions and more.

The `calculate_anything` module does not depend on `Ulauncher` or `Albert` so it is extensible for other use cases (see [demo with prompt_toolkit](#extending-and-more)).

See [Features](#features) for supported features, [Contents](#contents) for installation instructions and more

## Albert Demo

![Albert Demo](misc/demo-albert.gif)

## Ulauncher Demo 

![Ulauncher Demo](misc/demo-ulauncher.gif)

## Features

Calculator for Anything
- `Currency Converter`: See [Currency](#currency) for examples
- `Time Converter`: Convert time to other timezones and compute time expressions or find time remaining until any date-time. See [Time](#time) for examples.
- `Units Converter`: Compute and Convert units to other units. See [Units](#units) for examples.
- `Normal Calculator`: Supports functions such as `cos`, `sin`, `tan`. Check [Calculator](#calculator) for examples.
- `Complex Numbers` Calculator: Also supports Normal Calculator's functions. Check [Calculator](#calculator) for examples.
- `Percentage Calculator` Calculate percentages see [Percentages](#percentages) for examples.
    - Supports all expressions that Normal Calculator and Complex Calculator Support
- `Base N Calculator`: Calculate numbers and expressions to other number base. See [Base N Calculator](#base-n-calculator) for examples.
    - Base 16 (`hex`): Calculates expression to decimal, biniary, octal, color (i.e `RGB`, `YSV`, etc), Bytes (representation of `string`)
    - Base 2 (`bin`), Base 8 (`oct`), Base 10 (`dec`)
    - Supports functions: `or`, `xor`, `and`, `mod`, `div`, `+`, `-`, `/`  

**The only launcher specific files for `ulauncher` and `albert` are `main.py`, `__init__.py` in the root of this project**

**Dependencies**: [simpleeval](https://github.com/danthedeckie/simpleeval), [pint](https://pypi.org/project/Pint/) [parsedatetime](https://pypi.org/project/parsedatetime/) and [pytz](https://pypi.org/project/pytz/) (for parsedatetime)
Currency and Unit converter as well as a Calculator for numbers, complex numbers, percentages and time that supports mathematical functions and Complex Numbers.

Optional Dependencies: [babel](https://github.com/python-babel/babel). Installing this will format your results in your language/locale.

## Contents

 - [Install for Ulauncher](#install-for-ulauncher)
 - [Install for Albert](#install-for-albert)
 - [How to setup](#how-to-setup)
 - [Examples](#examples)
 - [Known Issues](#known-issues)
 - [Extending and more](#extending-and-more)


## Install for Ulauncher

Thus extension depends on [Pint](https://github.com/hgrecco/pint), [simpleeval](https://github.com/danthedeckie/simpleeval) and [parsedatetime](https://github.com/bear/parsedatetime). Install them with:
```bash
# You probably have some of them already installed
/usr/bin/python3 -m pip install Pint simpleeval parsedatetime pytz

# Optionally for translations and formatting to your locale
/usr/bin/python3 -m pip install babel
```

Open `Ulauncher` go to `Extensions` > `Add extension` and paste https://github.com/tchar/ulauncher-albert-calculate-anything

## Install for Albert

Similarly to `Ulauncher` the same dependencies are are required. Albert changed the way extensions work, so the `__init__.py` and the default install location had to be changed. I modified the bash install below to what they were changed to.

To install the extension for Albert run
```bash
# You probably have some of them already installed
/usr/bin/python3 -m pip install Pint simpleeval parsedatetime pytz

# Optionally for translations and formatting to your locale
/usr/bin/python3 -m pip install babel

# Determine Install location
[ -z "$XDG_DATA_HOME" ] && INSTALL_DIR=~/.local/share || INSTALL_DIR=$XDG_DATA_HOME

# Create module directory if not exists
mkdir -p $INSTALL_DIR/albert/python/plugins/modules/
# Before this was set to $INSTALL_DIR/albert/org.albert.extension.python/modules/

# Install extension
git clone https://github.com/caiofiga/ulauncher-albert-calculate-anything $INSTALL_DIR/albert/python/plugins/modules/
```

Open albert, enable `Python` extensions and then enable the `Calculate Anything` extension.

You can double click it to open module's location and edit `__init__.py` to add your preferences.
You can also edit the preferences  directly in Albert's Plugin config window.

## How to Setup

### Albert

If you are using Albert open the extension location normally at `~/.local/share/albert/org.albert.extension.python/modules/ulauncher-albert-calculate-anything/__init__.py` and edit the preferences mentioned below in the apropriate variable `API_KEY`, `CACHE`, `DEFAULT_CURRENCIES`, `DEFAULT_CITIES`, `SHOW_EMPTY_PLACEHOLDER` or `__triggers__` for the keyword

The extension can work in albert without keywords if you comment out the `__triggers__` option, however if another extension has the keyword you type, `Calculate Anything won't trigger` (see [relevant issue](https://github.com/albertlauncher/albert/issues/978))

### Ulauncher

If you are using Ulauncher use the extension preferences.

### Set Currency Provider

You can select from different currency providers. Supported providers are:
- [fixer.io](https://fixer.io/): You need an API Key (see [Set API Key](#set-api-key)). Get a free one at https://fixer.io/signup (go to your `fixer.io` dashboard and get your API key). This will include all providers from Internal
- Internal: If you select this option currencies are going to be fetched from a variety of providers like [coinbase](https://www.coinbase.com/), [mycurrency.net](https://www.mycurrency.net/) and [European Central Bank](https://www.ecb.europa.eu/home/html/index.en.html): No API key is requred.

Preferences:
- ULauncher: Select one in currency provider
- Albert: Modify the `CURRENCY_PROVIDER` in `__init__.py` to one of [`fixerio`, `internal` (European Central Bank)]

### Set API Key

In order for the currency conversion to work for providers that need an API Key, you need to set it in the preferences.
- ULauncher: Copy your api key to the `API KEY` box in preferences
- Albert: Modify the `API_KEY` in `__init__.py`


### Cache

For currency conversion you can enable the cache for a minimum of 1 day up to 1 year. This will store the results fetched by your currency provider to prevent redundant requests. This is especially helpful if you have a free plan on a paid currency provider that limits your requests. It will also display the results faster, since no request is made. If all requested currencies have been cached, no request is made.

- Ulauncher: Edit `Currency Cache` in the extension preferences
- Albert: Edit `CACHE=86400` in `__init__.py` and set it to your interval in seconds

### Default currency

In the preferences you can define a comma separated list of default currencies to show when typing conversion without target unit/currency.
Defaults to `USD,EUR,CAD,GBP,AUD`

- ULauncher: Edit in `Default Currencies` preferences
- Albert: Edit `DEFAULT_CURRENCIES` in `__init__.py`

### Default cities

In the preferences you can define a comma separated list of default cities when using the time command

- ULauncher: Edit in `Default Currencies` preferences
- Albert: Edit `DEFAULT_CITIES` in `__init__.py`

### Units Conversion Mode

In the preferences you can define a units conversion mode. For now there is normal (default) and crazy.

Crazy means that the unit converter/calculator tries to convert all possible units (currency included) available under the name.

See [Currency](#crazy-conversion) and [Units](#crazy-conversion-1) for more

**Crazy mode is experimental and bugs are to be expected**

- ULauncher: Edit in `Units Conversion mode` preferences
- Albert: Edit `UNITS_CONVERSION_MODE` in `__init__.py`

### Show Empty Placeholder

 - ULauncher: Default is `No`. Set to `Yes` to show an empty placeholder when extension doesn't return anything
 - Albert: Change `SHOW_EMPTY_PLACEHOLDER=True` in `__init__.py`

### Commands and Syntax

To calculate/convert anything you can use the keywords
- `=`: For currency, units and calculator
- `time`: For time calculations
- `dec`/`hex`/`bin`/`oct`: For base-n and calculations

You can go directly to [examples](#examples) or use the ones from the demo

To convert currency type your keyword and then

- `AMOUNT CURRENCY` to get conversion in the default currencies set in the preferences (requires cache)
- `AMOUNT CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`
- `CURRENCY in(or to) CURRENCY1,CURRENCY2,CURRENCY3`

To convert units use

- `AMOUNT UNIT in(or to) UNIT1,UNIT2,UNIT3`
- `UNIT in(or to) UNIT1,UNIT2,UNIT3`

Comma separated units and currencies can have spaces between them.

For time you can use the time keyword with a syntax

- `time` To get the current time plus the `default cities` you defined in the preferences
- `time at CITY,[COUNTRY|COUNTRY CODE|STATE CODE]` to get the current time for a specified city
- `time + AMOUNT [MONTH|YEAR|WEEK|DAY|HOUR|MINUTE|SECOND] [+ AMOUNT ...] [at CITY, [COUNTRY|COUNTRY CODE|STATE CODE]]` to get the time after the calculation at a specified city.

To calculate an expression just type your expression as in the demo
 - You can use functions such as `tan`,`atan`,`asinh`
 - You can use complex numbers too like `1 + 5i`

To calculate percentages you can use one of the following
- `AMOUNT1% of AMOUNT2` to calculate the AMOUNT1 percent of AMOUNT2
- `AMOUNT1 as % of AMOUNT2` to calculate AMOUNT1 as a percentage of AMOUNT2

If you select one results it will be copied to clipboard.

## Examples

### Currency

#### **Simple Conversion**
- Convert 10 euros to american dollars
    - `10 eur to USD`
    - `10 euros to $`
    - `10 eurs to dollars`

#### **Multiple Conversion**
- Convert 10 euros to american dollars, canadian dollars, bitcoin, and mexican pesos
    - `10 EUR to USD,canadian,bitcoin,mexican`

#### **Crazy Conversion**
`crazy` mode must be enabled in preferences
- Convert 1 us dollar per pound to euros per kilogram
    - `1 $ / pound to EUR / kg`
- Convert 10 us dollars  per square foot squared to canadian dollars per meter squared
    - `10 $ / foot ^ 2 to CAD / meter ^ 2`

### Time

You can also add and subtract time
For example if now is `2021-07-05 14:14:42` then you can use the following

Be careful to use date timespans like `2 years 5 months 2 weeks 3 days 1 hour 4 minutes 3 seconds` and not dates like `December 2022`.

**In the following examples the time returned is accompanied by the date time in the `default cities` you specified in the extension preferences**

- `time`: Returns 2021-07-05 14:14:42 as well as the date time in the default cities specified in settings
- `time plus 1 hour`: Returns Today at 15:14:42 
- `time + 1 day`: Returns Tomorrow at 14:14:42
- `time minus 1 day`: Returns Yesterday at 14:14:42
- `time + 2 hours` 2 minutes 5 seconds: Returns Today at 15:16:47
- `time + 1 year`: Returns 2022-07-05 14:14:42
- `time + 1 year 2 days 2 hours - 4 years 4 minutes`: Returns 2018-07-07 16:10:42

#### **Specifying a target city**

You can use all the commands above followed by `at CITY NAME` or `at CITY NAME, COUNTRY NAME|COUNTRY CODE|STATE CODE` to get te result in your local time as well as the specified city
- `time at Prague`
- `time + 2 hours at Madrid`
- `time + 2 hours at Vancouver, CA`: (There are two Vancouvers, so by specifying CA as returns the Canadian Vancouver)
- `time + 2 days 3 seconds at Vancouver, Canada`
- `time + 1 hour + 3 years at Athens, AL`: (Athens AL refers to Athens at Alabama)

#### **Using until**

You can also use the until command (**Experimental**) to calculate duration of time until a specific date

**Note: The midnight keyword shifts one day after, so midnight is considered to belong in the *next* day**

In the following examples you can specify a specific date and time or say for example a number of years months etc.

Keywords such as `a/next/last/previous/ago`, `years/months/weeks/days/hours/minutes/seconds`, `morning/noon/afternoon/evening/night/midnight`, `tomorrow/yesterday` and the combination of those will work like in the normal mode.

- `time until December 31 midnight`: Returns remaining days, hours minutes until January 00:00:00 (end of day for December)
- `time until midnight`: Returns remaining hours minutes seconds until midnight for this day (midnight is at 00:00:00)
- `time until tomorrow`: Day starts at 09:00
- `time until tomorrow evening`: Hours/Days until tomorrow at 18:00 
- `time until a year ago`: Negative result
- `time until 2000000 year`: Easter egg

And many more combinations

### Units

The units supported are all units that [pint](https://github.com/hgrecco/pint) supports (which is quite a lot)

#### **Simple Conversion**
- Convert 100 fahrenheit to celsius
   - `100 f to c`

#### **Multiple Conversion**
  - Convert 20 centimeters to inches and meters
    - `20 cm to inches, m`
    - `20 cm to inches,meters`

#### **Advanced Conversion**
- Convert kilometers per meter to centimeters per minute, kilometers per minute, inches per second and centimeters per second.
    - `20 km/h to cm/min, km/minute, in/s, cm/sec`
- Convert kilowhats per second to horsepower per hour and megawatts per second
    - `10 kw/sec to hp/h, mw/s`
- Convert meters per squared second to kilometers per squared hour
    - `10 m/s^2 to km/h^2`
- Convert megabytes per second to gigabytes per hour
    - `10 mb/s to gb/h`

**You can lieterally convert anything if the apropriate units match**
- Convert kilometer * centimeter * second per gibabyte to inches * meter * hour per megabyte
    - `10 km * cm * s / gb to inches * meter * hour / mb`

#### **Crazy Conversion**
`crazy` mode must be enabled in preferences
- `1 m to cm` may have two compatible units `meter` and `mole`, so it will return both results

### Percentages

#### **Simple Cases**
- Calculate what is 10% of 40
    - `10% of 40`: Answer is 4
- To calculate what percentage of 30 is 5, any of the following works
    - `5 is what % of 30`: Answer is 16.6667%
    - `5 is what % 30`
    - `5 as % of 30`
    - `5 in % of 30`
    - `5 in % 30`

#### **Advanced Cases**
- `10% of cos(pi) + 5`: Answer is 0.4
- `3 + 2 * pi % of cos(pi) + 5`: Answer is 0.371328
- `5 as % sqrt(2) + 5`: Answer is 77.9519%
- `1 + sin(pi) as % sqrt(2) + 5`: Answer is 15.5904%

### Calculator

The calculator works like a normal calculator, but is able to work with complex numbers too.

The following constants exist: `pi`, `e`, `tau` and others from [cmath](https://docs.python.org/3/library/cmath.html)

The following functions exist: `phase`, `polar`, `rect`, `exp`, `log`, `log10`, `sqrt`, `acos`, `asin`, `atan`, `cos`, `sin`, `tan`, `acosh`, `asinh`, `atanh`, `cosh`, `sinh`, `tanh` and others from [cmath](https://docs.python.org/3/library/cmath.html)

#### **Simple Cases**
- `10 + sqrt(2)`: Answer is 11.4142
- `10 + cos(pi) + 30 * e ^ 2`: Answer is 230.672

#### **Complex Numbers**
Use i as the imaginary unit
- `10 + sqrt(2) + i`: Answer is 11.4142 + i
- `cos(1 + i)`: Answer is 0.83373 - 0.988898i
- `e ^ (pi * i) + 1`: Answer is 0 (Euler's identity)

### Base N Calculator

Use with the keywords `hex`, `dec`, `bin`, `oct` by default.

#### **Simple Cases**
- `dec 1000`: Returns result in `hex`, `bin`, `oct`
- `hex ffa12`: Returns result in `dec`, `bin`, `oct` as well as `bytes` representation of the input query (including spaces)
- `bin 10101`: Returns result in `dec`, `hex`, `oct`

#### **Special cases with `hex`**
The hex calculator will always produce the `byte` representation of its input query.

#### **Color Conversion with `hex`**
If the input is in the format of #xxxxxx where xxxxxx is a valid hex number, it will convert the number representing a color to other color formats.
- `hex #fa1234`: Returns colors result in `rgb`, `hsv`, `hsl`, `cmyk`.

#### **Advanced Cases**
- `dec/hex/bin/oct 10101 and 10110 xor 10 + 1010 - 1010 div 10 and 10101`: Returns the result in all available base-n (`dec`, `hex`, `oct`, `bin`)
    - Digits must be valid in the base you are using (e.g 2012 is invalid for `bin`)

## Known Issues
If at any moment currency stops showing try removing the currency cache file and restart the Launcher/program

Linux
```bash
rm ~/.cache/com.github.tchar.calculate-anything/currency_data.json
```

Windows
```powershell
rm ~\AppData\Local\tchar\com.github.tchar.calculate-anything\Cache\currency_data.json
```
macOS
```zsh
rm ~/Library/Caches/com.github.tchar.calculate-anything/currency_data.json
```


## Extending and More

The calculate_anything module does not depend on ulauncher or albert, only the `main.py` (for Ulauncher) and `__init__.py` (for albert) do. You can extend it for other cases.

See the [documentation](docs/API.md) for API call examples

You can also find a sample usage of the API using [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) at the [prompt.py](misc/prompt.py) file.

Here is a demo

![](misc/demo-prompt_toolkit.gif)

### Adding flags

If your currencie's flag is missing you can place it in the extension's flags directory at `calculate_anything/images/flags/` and restart your launcher or make a pull request to include it.

Make sure to name your flag image in uppercase 2 letter name of your country. To make a currency flag, simply link the country flag you want to the currency `e.g ln -s US.svg USD.svg` or add a completely new flag For example American Dollar's flag is in `calculate_anything/images/flags/USD.svg`. You can use most image formats (i.e `svg`, `png`) 

<div>Flag Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
