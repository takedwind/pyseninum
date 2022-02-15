"""
===============================
 -*- coding:utf-8 -*-
 @Software: PyCharm
 @Author: Zoe
 @Email: 1120003477@qq.com
 @Time: 2021-05-25 10:06
 @File: page.py
 @Msg:页面对象开发
===============================
"""
# 页面属性封装（url、浏览器实例、元素、操作）
# 页面调用（页面继承、页面实例化）
# 基于页面调用的两种实现方式

from WebTest.common.browser import CHROME


# 页面基类
class Page:
    url = None # 子页面的初始访问地址
    driver = None

    def element(self,loc:tuple):
        """
        定位单个元素
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)

    def elements(self,loc:tuple):
        """
        定位一组元素或多个元素
        :param loc:
        :return:
        """
        return self.driver.find_elements(*loc)

# 基础公用页面
class ComLoginPage(Page):
    url = 'http://183.2.185.64:8000/zentao/user-login.html'
    driver = CHROME().browser
    username = ('id', 'account')
    password = ('name', 'password')
    loginBtn = ('id', 'submit')

    def get(self):
        """
        打开首页地址
        :return:
        """
        self.driver.get(self.url)

    def login(self,username: str="ybXborder",password: str="Kite1234"):
        self.element(self.username).send_keys(username)
        self.element(self.password).send_keys(password)
        self.element(self.loginBtn).click()

# 业务页面
class Search(ComLoginPage):
    searchInput = ('id','searchInput')
    searchGo = ('id','searchGo')
    user_name = ('xpath', '//span[@class="user-name"]')
    bug_label = ('xpath', '//span[@class="label label-id"]')
    log_out = ('xpath', '//a[text()="退出"]')


    def search_bug(self,bug_id: str="1"):
        self.element(self.searchInput).send_keys(bug_id)
        self.element(self.searchGo).click()


class TestSearch(Search):
    """
    测试登录和检索bug功能
    """
    def test_login(self):
        self.get()
        self.login()
        assert self.element(self.username).text == '龙远碧'
        print('test_login is ok')

    def test_search(self):
        self.search_bug()
        assert self.element(self.bug_label).text == '1'
        print('test_search is ok')
        self.driver.quit()


obj = TestSearch()
obj.test_login()
obj.test_search()
