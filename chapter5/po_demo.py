# 页面属性封装（url，浏览器实例，元素，操作）
# 页面调用（页面继承, 页面实例化）
# 基于页面调用可以有两种实现方式
from chapter3.bo import *
from setting import *
from chapter5.file_reader import YamlReader


class Page:

    url = None
    driver = None

    # 子类重写，获取通用配置文件中具体项目的元素配置文件字典
    # elements_yml = None
    elements_yml = {}

    # 缓存动态读取的yaml元素配置文件的解析结果
    elements_pool = {}

    def _locator(self, expression: str = 'cp.username'):
        """
        解析元素表达式的方法
        :param expression:
        :return:
        """
        name, value = expression.split('.')
        if name not in self.elements_yml:
            raise Exception('元素配置文件的别名：{}无法识别！'.format(name))

        if name not in self.elements_pool:
            self.elements_pool[name] = YamlReader(self.elements_yml[name]).data
            if (locator := self.elements_pool[name][value])[0] not in BY_RULES:
                raise Exception(
                    f'无法识别定位方法：{locator}'
                )
            return locator
        return self.elements_pool[name][value]

    @classmethod
    def cls_locator(cls, expression: str = 'cp.username'):
        return []

    @classmethod
    def cls_element(cls, loc: str):
        return cls.driver.find_element(*cls.cls_locator(loc))

    def element(self, loc: str):
        """
        定位元素的方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*self._locator(loc))

    def elements(self, loc: str):
        """
        定位一组元素或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*self._locator(loc))


class CommonLoginPage(Page):

    url = PROJECT_ZenTao_URL
    driver = CHROME().browser
    # username = ('id', 'account')
    # password = ('name', 'password')
    # loginBtn = ('id', 'submit')
    elements_yml = YAML_ELEMENT

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    @classmethod
    def cls_get(cls):
        """
        类方法,打开首页
        :return:
        """
        cls.driver.get(cls.url)

    def login(self, username: str = 'admin', password: str = 'admin123456'):
        self.element('cp.username').send_keys(username)
        # self.element(self.username).send_keys(username)
        # self.element(self.password).send_keys(password)
        # self.element(self.loginBtn).click()
        self.element('cp.password').send_keys(password)
        self.element('cp.loginBtn').click()

    @classmethod
    def cls_login(cls, username: str = 'admin', password: str = 'admin123456'):
        cls.cls_element('cp.username').send_keys(username)
        cls.cls_element('cp.password').send_keys(password)
        cls.cls_element('cp.loginBtn').click()


class Search(CommonLoginPage):

    # searchInput = ('id', 'searchInput')
    # searchGo = ('id', 'searchGo')
    # user_name = ('xpath', '//span[@class="user-name"]')
    # bug_label = ('xpath', '//span[@class="label label-id"]')
    # log_out = ('xpath', '//a[text()="退出"]')

    def search_bug(self, bug_id: str = '1'):
        self.element('sp.searchInput').send_keys(bug_id)
        self.element('sp.searchGo').click()

    def logout(self):
        self.element('sp.user_name').click()
        self.element('sp.log_out').click()


class TestSearch(Search):
    """
    测试登录和检索bug功能
    """
    def test_login(self):
        self.get()
        self.login()
        assert self.element('sp.user_name').text == 'admin'
        print('test_login is ok')

    def test_search(self):
        self.search_bug()
        assert self.element('sp.bug_label').text == '1'
        print('test_search is ok')
        self.driver.quit()


# obj = TestSearch()
# obj.test_login()
# obj.test_search()
