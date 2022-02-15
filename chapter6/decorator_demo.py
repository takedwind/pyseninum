from functools import wraps


def func_2(func):
    """
    无参的函数装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def wrap_func(*args, **kwargs):
        print('开始执行：' + func.__name__)
        func(*args, **kwargs)
        print('执行完成：' + func.__name__)
    return wrap_func


def func_3(arg=True):
    """
    有参的函数装饰器
    :param arg:
    :return:
    """
    def inner_func(func):
        @wraps(func)
        def wrap_func(*args, **kwargs):
            print('开始执行：' + func.__name__) if arg else print('...')
            func(*args, **kwargs)
            print('执行完成：' + func.__name__)

        return wrap_func
    return inner_func


@func_3(False)
# @func_2
def func_1():
    """
    业务函数
    :return:
    """
    print('正在执行：' + func_1.__name__)


# @func_2 == func_2(func_1) ===> wrap_func

# func_1() == wrap_func()

func_1()
