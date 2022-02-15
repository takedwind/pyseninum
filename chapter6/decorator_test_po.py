from chapter5.po_demo import Search
import unittest
from .decorators import depend, logs


class TestSearch(unittest.TestCase, Search):
    """
    测试登录和检索bug功能
    """
    @logs
    def test_login(self):
        self.get()
        self.login(password='123')
        assert self.element('sp.user_name').text == 'admin'
        print('test_login is ok')
        self.logout()

    @depend('test_login')
    def test_search(self):
        self.login()
        self.search_bug()
        assert self.element('sp.bug_label').text == '1'
        print('test_search is ok')


if __name__ == '__main__':
    unittest.main()
