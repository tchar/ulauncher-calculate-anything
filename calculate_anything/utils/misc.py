'''Miscellaneous utility functions'''

from typing import (
    Any,
    Callable,
    Container,
    Iterator,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)
import sys

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol
from contextlib import contextmanager
from functools import lru_cache, wraps
import os
from threading import RLock
from types import ModuleType
import importlib
from calculate_anything import logging
from calculate_anything.exceptions import MissingSimpleevalException


__all__ = [
    'get_module',
    'is_types',
    'is_not_types',
    'get_or_default',
    'is_integer',
    'StupidEval',
    'safe_operation',
    'with_lock',
]


RT = TypeVar('RT')


def get_module(name: str) -> Union[None, ModuleType]:
    '''Returns a module based on its name.

    Args:
        name (str): The name of the module.

    Returns:
        Union[ModuleType, None]: The module or None if not found.
    '''
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        return None


def is_types(*types: Type[Any]) -> Callable[[Any], bool]:
    '''Check if a value is of type. Useful for maps and filters.

    Args:
        types (Any): The type to check against.

    Returns:
        callable: A function which takes as a parameter a value
            and checks if the value is of any of the provided types.
    '''
    return lambda value: isinstance(value, types)


def is_not_types(*types: List[Type[Any]]) -> bool:
    '''Check if a value is not of type. Useful for maps and filters.

    Args:
        types (Any): The type to check against.

    Returns:
        callable: A function which takes as a parameter a value
            and checks if the value is not of any of the provided types.
    '''
    return lambda value: not is_types(*types)(value)


def get_or_default(
    value: Any,
    _type: Type[Any],
    default: Any,
    allowed_values: Optional[Container] = None,
) -> Any:
    '''Return a value if it is of specified type and in allowed values

    Args:
        value (Any): The value to check.
        type (Any): The type to check the value against.
        default (Any): Default value to return if value does not match
            type or in allowed values.
        allowed_values (contianer, optional): Allowed values for the value
            provided. If None or nothing is provided it will not be used.

    Returns:
        Any: The value as a type of the provided type, or default if
            value was not of the provided type, or in allowed types.
    '''
    try:
        value = _type(value)
        if allowed_values and value not in allowed_values:
            return default
        return value
    except Exception:
        return default


def is_integer(value: Any) -> bool:
    '''Checks if a value is integer with extra functionality.
    If the provided value is a complex number the imaginary part
    is checked. If the value is boolean False is returned.

    Args:
        value (Any): The value to check for integer.

    Returns:
        bool: If it is an integer or not.
    '''
    if isinstance(value, float):
        if value.is_integer():
            return True
        return False
    if isinstance(value, complex):
        return value.imag == 0
    if isinstance(value, bool):
        return False
    return isinstance(value, int)


class StupidEval:
    '''Mock class replacement for SimpleEval if simpleeval is not installed.'''

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.operators = {}

    @staticmethod
    def _try_parse(query, _type):
        try:
            return _type(query)
        except (ValueError, TypeError):
            return None

    def eval(self, query: str) -> Union[int, complex, float]:
        '''Evalutes the expression as integer, float or complex.

        Args:
            query (str): The query to evaluate.

        Returns:
            Union[int, float, complex]: The evaluated query.

        Raises:
            MissingSimpleevalException: If query cannot be evaluated.
        '''
        if not isinstance(query, str):
            raise MissingSimpleevalException
        value = StupidEval._try_parse(query, int)
        if value is not None:
            return value
        value = StupidEval._try_parse(query, float)
        if value is not None:
            return value
        value = StupidEval._try_parse(query, complex)
        if value is not None:
            return value
        raise MissingSimpleevalException


@contextmanager
def safe_operation(message: str = '') -> Iterator[None]:
    '''Context manager for safe operations to catch any errors.

    Args:
        message (str, optional): The message to log. If not provided no log is
            made.
    '''
    logger = logging.getLogger(__name__)
    if message:
        logger.info(message)
    try:
        yield
    except Exception as e:
        msg = e
        if message:
            msg = '{}: {}'.format(message, e)
        logger.exception('Got error in safe operation: {}'.format(msg))


class LockableClass(Protocol):
    lock: RLock


def with_lock(func: Callable[..., RT]) -> Callable[..., RT]:
    '''Method decorator for classes that use locks. The class should
    have a property called 'lock' and the lock should be a contextmanager.
    (i.e threading.RLock).

    Args:
        func (LockableCallable): A method to decorate

    Returns:
        LockableCallable: The method decorated with lock.
    '''

    @wraps(func)
    def _wrapper(self: LockableClass, *args: Any, **kwargs: Any) -> Any:
        with self.lock:
            return func(self, *args, **kwargs)

    return _wrapper


@lru_cache(maxsize=20)
def images_dir(*paths):
    return os.path.join('calculate_anything', "images", *paths)
