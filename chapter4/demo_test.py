import unittest
from time import sleep
from chapter3.po_demo import Search
import paramunittest

#
# @paramunittest.parametrized(
#     ('admin', 'admin123456', 'admin', 'test_login_admin is ok'),
#     ('json', 'json123456', 'json', 'test_login_json is ok'),
#     ('tom', 'tom123456', 'tom', 'test_login_tom is ok')
# )
# class TestSearch(unittest.TestCase, Search):
#
#     def setParameters(self, name, pwd, ass, txt):
#         self.name = name
#         self.pwd = pwd
#         self.ass = ass
#         self.txt = txt
#
#     def test_login(self):
#         self.get()
#         self.login(self.name, self.pwd)
#         sleep(1)
#         assert self.element(self.user_name).text == self.ass
#         print(self.txt)
#         self.logout()
#         sleep(1)

    #
    # def test_login_admin(self):
    #     self.get()
    #     self.login('admin', 'admin123456')
    #     sleep(1)
    #     assert self.element(self.user_name).text == 'admin'
    #     print('test_login_admin is ok')
    #     self.logout()
    #     sleep(1)
    #
    # def test_login_json(self):
    #     # self.get()
    #     self.login('json', 'json123456')
    #     sleep(1)
    #     assert self.element(self.user_name).text == 'json'
    #     print('test_login_json is ok')
    #     self.logout()
    #     sleep(1)
    #
    # def test_login_tom(self):
    #     # self.get()
    #     self.login('tom', 'tom123456')
    #     sleep(1)
    #     assert self.element(self.user_name).text == 'tom'
    #     print('test_login_tom is ok')
    #     self.driver.quit()


data = (
    {'name': 'admin', 'pwd': 'admin123456', 'ass': 'admin', 'txt': 'test_login_admin is ok'},
    {'name': 'json', 'pwd': 'json123456', 'ass': 'json', 'txt': 'test_login_json is ok'},
    {'name': 'tom', 'pwd': 'tom123456', 'ass': 'tom2', 'txt': 'test_login_tom is ok'}
)


class A(unittest.TestCase, Search):

    def test_login(self):
        for d in data:
            with self.subTest(d):
                self.get()
                self.login(d['name'], d['pwd'])
                sleep(1)
                # assert self.element(self.user_name).text == d['ass'], \
                #     self.driver.save_screenshot(f'./{d["ass"]}.png')
                try:
                    self.assertEqual(self.element(self.user_name).text, d['ass'])
                except AssertionError:
                    self.driver.save_screenshot(f'./{d["ass"]}.png')
                    raise AssertionError
                print(d['txt'])
                self.logout()
                sleep(1)


if __name__ == '__main__':
    unittest.main()
