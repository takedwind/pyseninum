from aiohttp import ClientSession
from chapter9.async_webdriver import AsyncBrowser
from types import FunctionType
from typing import List, Tuple, Dict, AnyStr
import asyncio


async def async_func(func_list: List[FunctionType], *args, **kwargs):
    async with ClientSession() as session:
        driver = await AsyncBrowser.start(*args, **kwargs, http_session=session)
        async with driver as _driver:
            for func in func_list:
                await func(_driver)


async def async_cls(cls_list, *args, **kwargs):
    async with ClientSession() as session:
        driver = await AsyncBrowser.start(*args, **kwargs, http_session=session)
        async with driver as _driver:
            for cls in cls_list:
                cls.async_driver = _driver
                instance = cls()
                _attr_list = dir(instance)
                for attr in _attr_list:
                    if 'test' in attr:
                        await eval(f'instance.{attr}()')


async def async_run_func(*args):
    await asyncio.gather(*[async_func(*func_url_caps) for func_url_caps in args])


async def async_run_cls(*args):
    await asyncio.gather(*[async_cls(*cls_url_caps) for cls_url_caps in args])


def main_func(main_fields: List[Tuple[List, AnyStr, Dict]]):
    """
    main_fields = [
        ([test_case1, test_case2, ...], 'url', cap),
        ()
    ]
    :param main_fields:
    :return:
    """
    asyncio.run(async_run_func(*main_fields))


def main_cls(main_fields: List[Tuple[List, AnyStr, Dict]]):
    """
    main_fields = [
        ([test_cls1, test_cls2, ...], 'url', cap),
        ()
    ]
    :param main_fields:
    :return:
    """
    asyncio.run(async_run_cls(*main_fields))
