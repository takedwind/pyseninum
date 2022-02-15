# 页面属性封装（url，浏览器实例，元素，操作）
# 页面调用（页面继承, 页面实例化）
# 基于页面调用可以有两种实现方式

from chapter3.bo import *
from setting import *
from chapter5.file_reader import YamlReader


class Page:

    url = None
    locators = {}
    browser = CHROME

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            self.driver = self.browser().browser

    def __getattr__(self, loc):
        if loc not in self.locators.keys():
            raise Exception

        by, val = self.locators[loc]

        return self.driver.find_element(by, val)


class CommonLoginPage(Page):

    url = PROJECT_ZenTao_URL
    # locators = {
    #     'username': ('id', 'account'),
    #     'password': ('name', 'password'),
    #     'loginBtn': ('id', 'submit')
    # }
    locators = YamlReader(YAML_ELEMENT['cp']).data

    def get(self):
        """
        打开项目地址
        :return:
        """
        self.driver.get(self.url)

    def login(self, username: str = 'admin', password: str = 'admin123456'):
        self.username.send_keys(username)
        self.password.send_keys(password)
        self.loginBtn.click()


class MainPage(CommonLoginPage):

    # CommonLoginPage.locators.update({
    #     'searchInput': ('id', 'searchInput'),
    #     'searchGo': ('id', 'searchGo'),
    #     'user_name': ('xpath', '//span[@class="user-name"]'),
    #     'bug_label': ('xpath', '//span[@class="label label-id"]')
    # })
    CommonLoginPage.locators.update(
        YamlReader(YAML_ELEMENT['sp']).data
    )

    def search_bug(self, bug_id: str = '1'):
        self.searchInput.send_keys(bug_id)
        self.searchGo.click()


class TestMain:

    def test_login(self):
        page = MainPage()
        page.get()
        page.login()
        assert page.user_name.text == 'admin'
        print('test login is ok')
        page.driver.quit()

    def test_search(self):
        page = MainPage()
        page.get()
        page.login()
        page.search_bug()
        assert page.bug_label.text == '1'
        print('test search is ok')
        page.driver.quit()


obj = TestMain()
obj.test_login()
obj.test_search()
