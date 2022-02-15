import unittest
from chapter3.po_demo import Search
from time import sleep


class TestA(unittest.TestCase, Search):

    @classmethod
    def setUpClass(cls) -> None:
        ...

    def setUp(self) -> None:
        self.get()
        self.login()
        sleep(2)

    def test_search(self):
        sleep(2)
        self.search_bug()
        assert self.element(self.bug_label).text == '1'

    def test_logout(self):
        sleep(2)
        self.logout()
        assert self.driver.current_url == 'http://127.0.0.1/zentao/user-login.html'

    def tearDown(self) -> None:
        sleep(2)
        self.driver.refresh()


class B(unittest.TestCase, Search):

    @classmethod
    def setUpClass(cls) -> None:
        cls.cls_get()
        cls.cls_login()
        sleep(2)

    def setUp(self) -> None:
        ...

    def test_search(self):
        sleep(2)
        self.login()
        self.search_bug()
        assert self.element(self.bug_label).text == '1'

    def test_logout(self):
        sleep(2)
        self.logout()
        assert self.driver.current_url == 'http://127.0.0.1/zentao/user-login.html'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
