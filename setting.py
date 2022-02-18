# 项目地址
# 项目包和文件夹的路径
# 浏览器对象属性
# 测试套件
from os.path import dirname, join

# ---------------------项目地址---------------------
# 项目一地址
PROJECT_ZenTao_URL = 'http://127.0.0.1/zentao/user-login.html'

# 项目二地址
PROJECT_QQ_URL = ''

# 项目三地址
PROJECT_DEMO_URL = ''
# ---------------------项目地址---------------------

# ---------------------项目包和文件夹的路径---------------------
# 项目根目录
BASE_PATH = dirname(__file__)

# 浏览器驱动文件地址
CHROME_DRIVER_PATH = join(BASE_PATH, 'drivers/chrome_driver.exe')
EDGE_DRIVER_PATH = join(BASE_PATH, 'drivers/edge_driver.exe')
FIREFOX_DRIVER_PATH = join(BASE_PATH, 'drivers/gecko_driver.exe')
IE_DRIVER_PATH = join(BASE_PATH, 'drivers/IEDriverServer.exe')
OPERA_DRIVER_PATH = join(BASE_PATH, 'drivers/opera_driver.exe')

# 项目模块路径
# 模块1路径
CHAPTER_1_PATH = join(BASE_PATH, 'chapter3')

# 模块2路径
CHAPTER_2_PATH = join(BASE_PATH, 'chapter4')

# 模块3路径
CHAPTER_3_PATH = join(BASE_PATH, 'chapter5')

# 元素配置文件的根目录
ELEMENTS_YAML_FILE_PATH = join(BASE_PATH, 'chapter5/page')

# 数据库配置文件路径
DATABASE_INI_PATH = join(BASE_PATH, 'chapter8/database.ini')
# ---------------------项目包和文件夹的路径---------------------

# ---------------------测试套件---------------------
# 流程1相关测试套件
SUIT_MODULE_1 = ['module_1_test.py', 'module_2_test.py']

# 流程2相关测试套件
SUIT_MODULE_2 = ['module_1_test.py', 'module_2_test.py', 'module_3_test.py']

# 流程3相关测试套件
SUIT_MODULE_3 = ['module_4_test.py', 'module_5_test.py']

# 项目一主测试套件
SUIT_PROJECT1 = ['module_1_test.py', 'module_2_test.py', 'module_3_test.py']

# 项目二的主测试套件
SUIT_PROJECT2 = SUIT_MODULE_2 + SUIT_MODULE_3
# ---------------------测试套件---------------------

# ---------------------浏览器对象属性---------------------
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
WINDOWS_SIZE = (1920, 1024)

# ---------CHROME浏览器属性--------
# chrome浏览器操作开关
CHROME_METHOD_MARK = True

# chrome启动参数开关
CHROME_OPTION_MARK = True

# chrome实验性质启动参数
CHROME_EXPERIMENTAL = {
        # 'mobileEmulation': {'deviceName': 'iPhone 6'},
        'excludeSwitches': ['enable-automation']
    }

# chrome窗口大小启动参数
CHROME_WINDOW_SIZE = ''

# chrome启动最大化参数
CHROME_START_MAXIMIZED = '--start-maximized'

# chrome隐式等待时间
CHROME_IMPLICITLY_WAIT_TIME = 30
# ---------CHROME浏览器属性--------

# ---------IE浏览器属性--------
# ie浏览器启动参数开关
IE_MARK = True

# ie浏览器清空本地会话
IE_CLEAN_SESSION = True

# ie页面超时时间
IE_ATTACH_TIMEOUT = 10000
# ---------IE浏览器属性--------

# ---------FIREFOX浏览器属性--------
# ---------FIREFOX浏览器属性--------

# ---------OPERA浏览器属性--------
# ---------OPERA浏览器属性--------

# ---------------------浏览器对象属性---------------------

# ---------------------YAML元素配置文件---------------------
YAML_ELEMENT = {
    'cp': join(ELEMENTS_YAML_FILE_PATH, 'common_login_page.yml'),
    'sp': join(ELEMENTS_YAML_FILE_PATH, 'search_page.yml')
}
# ---------------------YAML元素配置文件---------------------
# print(YAML_ELEMENT)

# ---------------------WEB元素定位方法---------------------
BY_RULES = (
    'id',
    'xpath',
    'link text',
    'partial link text',
    'name',
    'tag name',
    'class name',
    'css selector'
)
# ---------------------WEB元素定位方法---------------------
