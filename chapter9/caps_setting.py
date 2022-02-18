CHROME_CAPS = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'chrome',
            'platformName': 'any',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            },
            'goog:chromeOptions': {
                'excludeSwitches': ['enable-automation'],
                # 'mobileEmulation': {'deviceName': 'iPhone 6'},
                'args': [
                    '--start-maximized',
                    # '--headless'
                ],
                'prefs': {
                    # 禁用密码保存弹框
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }
            }
        }
    }
}

CHROME_CAPS_2 = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'chrome',
            'platformName': 'any',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            },
            'goog:chromeOptions': {
                'excludeSwitches': ['enable-automation'],
                # 'mobileEmulation': {'deviceName': 'iPhone 6'},
                # 'args': [
                #     '--start-maximized',
                #     # '--headless'
                # ],
                'prefs': {
                    # 禁用密码保存弹框
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }
            }
        }
    }
}

FIREFOX_CAPS = {
    'capabilities': {
        'firstMatch': [{}],
        'alwaysMatch': {
            'browserName': 'firefox',
            'platformName': 'windows',
            'timeouts': {
                'implicit': 30000,
                'pageLoad': 300000,
                'script': 30000
            }
        }
    }
}
