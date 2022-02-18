from selenium.webdriver.chrome.service import Service as Chrome_Service
from selenium.webdriver.firefox.service import Service as Firefox_Service
from setting import FIREFOX_DRIVER_PATH, CHROME_DRIVER_PATH
from chapter9.async_test_func import test_search, test_login
from chapter9.async_test_cls import AsyncTestMain, AsyncTestLogin
from chapter9.async_main import main_cls
from chapter9.caps_setting import *


chrome_service = Chrome_Service(CHROME_DRIVER_PATH)
chrome_service.start()
chrome_url = chrome_service.service_url

firefox_service = Firefox_Service(FIREFOX_DRIVER_PATH)
firefox_service.start()
firefox_url = firefox_service.service_url

test_suit_func = [
    ([test_login, ], chrome_url, CHROME_CAPS),
    ([test_search, ], chrome_url, CHROME_CAPS_2),
    ([test_search, ], firefox_url, FIREFOX_CAPS)
]

test_suit_cls = [
    ([AsyncTestLogin, ], chrome_url, CHROME_CAPS),
    # ([AsyncTestMain, ], chrome_url, CHROME_CAPS_2),
    ([AsyncTestMain, ], firefox_url, FIREFOX_CAPS)
]

# main_func(test_suit_func)
main_cls(test_suit_cls)
