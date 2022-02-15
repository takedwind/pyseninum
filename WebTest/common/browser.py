"""
===============================
 -*- coding:utf-8 -*-
 @Software: PyCharm
 @Author: Zoe
 @Email: 1120003477@qq.com
 @Time: 2021-05-23 10:06
 @File: page.py
 @Msg:浏览器对象开发
===============================
"""
# 浏览器的类型browser_type(chrome,ie,firefox,edge,opera)
# 浏览器的启动参数（无头化，最大化，尺寸化）
# 浏览器的属性（显示尺寸，隐式等待/页面加载/js执行时间）

from selenium.webdriver import *
from typing import Type, Union
from WebTest.common.setting import *


class BrowserTypeError(Exception):
    def __init__(self, _type):
        self._type = _type

    def __str__(self):
        return f"unsupported browser type:{self._type}"


class BROWSER:

    CHROME_DRIVER_PATH = CHROME_DRIVER_PATH
    # 使用32位ie驱动解决文本输入缓慢的问题
    IE_DRIVER_PATH = IE_DRIVER_PATH
    FIREFOX_DRIVER_PATH = FIREFOX_DRIVER_PATH
    EDGE_DRIVER_PATH = EDGE_DRIVER_PATH
    OPERA_DRIVER_PATH = OPERA_DRIVER_PATH

    WINDOWS_SIZE = (1024,900)
    IMP_TIME = 30 #
    PAGE_LOAD_TIME = 20 # 页面加载时间
    SCRIPT_TIME_OUT = 20
    HEADLESS = True # 无头化启动

    def __init__(self, browser_type: Type[Union[Firefox, Chrome, Ie, Edge, Opera]] = Chrome,
                 option_type: Type[Union[FirefoxOptions, ChromeOptions, IeOptions]] = ChromeOptions,
                 driver_path: str = CHROME_DRIVER_PATH):
        """
        :param browser_type: 浏览器类型
        :param option_type: 操作类型
        :param driver_path: 浏览器driver路径
        """
        if not issubclass(browser_type, (Firefox, Chrome, Ie, Edge, Opera)):
            raise BrowserTypeError(browser_type)
        if not issubclass(option_type, (FirefoxOptions, ChromeOptions, IeOptions)):
            raise BrowserTypeError(option_type)
        if not isinstance(driver_path, str):
            raise TypeError

        self._browser = browser_type
        self._option = option_type
        self._path = driver_path

    @property
    def options(self):
        """
        浏览器特定的操作，在子类中实现
        :return:
        """
        return

    @property
    def browser(self):
        """
        启动浏览器，返回浏览器实例
        :return:
        """
        return


class CHROME(BROWSER):
    HEADLESS = False  # 不需要无头化启动
    IMP_TIME = 30 # 隐式等待时间
    PAGE_LOAD_TIME = 30 # 页面加载时间
    SCRIPT_TIME_OUT = 30 # 异步js执行时间
    # WINDOWS_SIZE = '--window-size=1920,1080' # 窗口尺寸
    START_MAX = '--start--maximinzed' # chrome_option启动参数
    EXP = {
        'excludeSwitches':['enable-automation'],
        'mobileEmulation':{'deviceName':'iPhone 6'}
    }

    @property
    def options(self):
        chrome_option = self._option()
        chrome_option.add_argument(self.START_MAX)
        for k,v in self.EXP.items():
            chrome_option.add_experimental_option(k,v)
        chrome_option.headless = self.HEADLESS
        return chrome_option

    @property
    def browser(self): #  启动浏览器，返回浏览器实例
        chrome = self._browser(self._path,options=self.options)
        chrome.implicitly_wait(self.IMP_TIME)
        chrome.set_page_load_timeout(self.PAGE_LOAD_TIME)
        # chrome.set_window_size(*self.WINDOWS_SIZE)
        return chrome

# 调试chrome
# with CHROME().browser as _chrome:
#     _chrome.get('http://183.2.185.64:8000/zentao/user-login.html')
#     from time import sleep
#     sleep(3)


class IE(BROWSER):
    CLEAN_SESSION = True # 是否清理缓存

    def __init__(self):
        super(IE,self).__init__(
            browser_type=Ie,
            option_type=IeOptions,
            driver_path= super().IE_DRIVER_PATH
        )

    @property
    def options(self):
        ie_option = self._option()
        ie_option.ensure_clean_session = self.CLEAN_SESSION
        return ie_option

    @property
    def browser(self):
        ie = self._browser(self._path,options=self.options)
        ie.implicitly_wait(self.IMP_TIME)
        ie.set_page_load_timeout(self.PAGE_LOAD_TIME)
        ie.set_script_timeout(self.SCRIPT_TIME_OUT)
        ie.maximize_window()
        return ie

# with IE().browser as _ie:
#     _ie.get('http://183.2.185.64:8000/zentao/user-login.html')
#     from time import sleep
#     sleep(3)










