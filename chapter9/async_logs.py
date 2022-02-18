from functools import wraps
from chapter6.decorators import log


def logs(func):
    """
    异步日志装饰器
    :param func:
    :return:
    """
    @wraps(func)
    async def wrap_func(*args, **kwargs):
        tuple_args = args
        dict_kwargs = kwargs
        try:
            await func(*args, **kwargs)
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
