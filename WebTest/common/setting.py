"""
===============================
 -*- coding:utf-8 -*-
 @Software: PyCharm
 @Author: Zoe
 @Email: 1120003477@qq.com
 @Time: 2021-06-11 17:32
 @File: setting.py
 @Msg:
        # 项目地址
        # 项目包和文件夹路径
        # 浏览器对象属性
        # 测试套件
===============================
"""

import os
# -----------------------------项目地址-----------------------------------------

PROJECT_ZENTAO_URL = 'http://183.2.185.64:8000/zentao/'

# -----------------------------项目包和文件夹的路径-------------------------------
# 项目根目录
BASE_PATH = os.path.dirname(__file__)
# 浏览器驱动文件地址
CHROME_DRIVER_PATH = os.path.join(BASE_PATH,'/drivers/chrome_driver.exe')
IE_DRIVER_PATH = os.path.join(BASE_PATH,"../drivers/IEDriverServer_32.exe")
FIREFOX_DRIVER_PATH = os.path.join(BASE_PATH,"../drivers/gecko_driver.exe")
EDGE_DRIVER_PATH = os.path.join(BASE_PATH,"../drivers/edge_driver.exe")
OPERA_DRIVER_PATH = os.path.join(BASE_PATH,"../drivers/opera_driver.exe")

# 项目模块路径
CHAPTER_1_PATH =  os.path.join(BASE_PATH,".chapter1")

# -----------------------------测试套件-----------------------------------------
# 流程1相关测试套件
SUIT_MODULE_1 = ['module_1_test.py','module_2_test.py']
# 流程2相关测试套件
SUIT_MODULE_2 = ['module_1_test.py','module_2_test.py','module_3_test.py']
# 流程3相关测试套件
SUIT_MODULE_3 = ['module_4_test.py','module_5_test.py','module_6_test.py']
# 主测试套件
SUIT_PROJECT = SUIT_MODULE_2 + SUIT_MODULE_3

# -----------------------------浏览器对象属性-----------------------------------------
# 浏览器基本属性
# 无头化
HEADLESS = False

# 隐式等待时间
IMPLICITLY_WAIT_TIME = 20

# 页面加载超时时间
PAGE_LOAD_TIME = 20

# JS异步执行超时时间
SCRIPT_TIMEOUT = 20

# 浏览器启动尺寸
WINDOWS_SIZE = (1920,1024)

# -----------------------------CHROME浏览器特有属性--------------------------------------
# chrome 浏览器操作开关
CHROME_METHOD_MARK = True
# chrome启动参数开关
CHROME_OPTION_MARK = True
# chrome实验化性质启动参数
CHROME_EXPERIMENTAL = {
    # 'mobileEmulation':{'deviceName':'iPhone 6'},
    'excludeSwitches':['enable-automation']
}
# chrome窗口大小启动参数
CHROME_WINDOW_SIZE =''
# chrome启动最大化参数
CHROME_START_MAXIMIZED = '--start--maximinzed'

# chrome隐式等待时间
CHROME_IMPLICITLY_WAIT_TIME = 30



# -----------------------------FIREFOX浏览器特有属性--------------------------------------

# ie 浏览器启动参数开关
IE_MARK = True
# ie 浏览器清空本地会话
IE_CLEAN_SESSION = True
# ie页面超时时间
IE_ATTACH_TIMEOUT = 10000



# -----------------------------IE浏览器特有属性--------------------------------------


# -----------------------------EDGE浏览器特有属性--------------------------------------



# -----------------------------OPERA浏览器特有属性--------------------------------------


