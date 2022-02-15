from functools import wraps
import unittest
from chapter6.logs import log
from selenium.common.exceptions import WebDriverException


class DependencyError(Exception):

    def __int__(self, _type=0):
        self._type = _type

    def __str__(self):
        if self._type == 0:
            return f'Dependency name of test is required!'
        if self._type == 1:
            return f'Dependency name of test can not the case self!'


def depend(case=''):
    if not case:
        raise DependencyError
    _mark = []

    def wrap_func(func):
        @wraps(func)
        def inner_func(self):
            if case == func.__name__:
                raise DependencyError(1)
            _r = self._outcome.result
            _f, _e, _s = _r.failures, _r.errors, _r.skipped

            if not (_f or _e or _s):
                func(self)

            if _f:
                _mark.extend([fail[0] for fail in _f])
            if _e:
                _mark.extend([error[0] for error in _e])
            if _s:
                _mark.extend([skip[0] for skip in _s])

            unittest.skipIf(
                case in str(_mark),
                f'The pre-depend case :{case} has failed! Skip the specified case!'
            )(func)(self)
        return inner_func
    return wrap_func
#
# @unittest.skipIf(case in str(_mark), '')
# def test(self):
#     ...
# unittest.skipIf(case in str(_mark), '')(test)


# def logs(func):
#     """
#     普通日志装饰器
#     :param func:
#     :return:
#     """
#     @wraps(func)
#     def wrap_func(*args, **kwargs):
#         tuple_args = args
#         dict_kwargs = kwargs
#         func(*args, **kwargs)
#         log.debug(
#             f'{func.__name__}(*args: tuple = *{tuple_args}, **kwargs: dict = **{dict_kwargs})',
#             extra={'status': 'PASS'}
#         )
#     return wrap_func


def logs(func):
    """
    兼容日志装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrap_func(*args, **kwargs):
        tuple_args = args
        dict_kwargs = kwargs
        try:
            func(*args, **kwargs)
            log.debug(
                f'{func.__name__}(*args: tuple = *{tuple_args}, **kwargs: dict = **{dict_kwargs})',
                extra={'status': 'PASS'}
            )
        except Exception:
            log.exception(
                f'{func.__name__}(*args: tuple = *{tuple_args}, **kwargs: dict = **{dict_kwargs})',
                exc_info=True,
                extra={'status': 'FAIL'}
            )
            raise

    return wrap_func
