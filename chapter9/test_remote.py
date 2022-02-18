from chapter9.async_test_func import test_search, test_login
from chapter9.async_test_cls import AsyncTestMain, AsyncTestLogin
from chapter9.async_main import main_cls
from chapter9.caps_setting import *


chrome_url = r'http://localhost:9515'
firefox_url = r'http://localhost:4444'


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
