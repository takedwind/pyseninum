import unittest


class A(unittest.TestCase):

    def test_a(self):
        assert (_len := self.test_a.__name__.__len__()) == 4, \
            print(f'test_a方法名称的长度是：{_len}， 不等于4！')

    def test_b(self):
        _len = None
        try:
            self.assertEqual((_len := self.test_b.__name__.__len__()), 4)
        except AssertionError:
            print(f'test_b方法名称的长度是：{_len}， 不等于4！')
            raise AssertionError(f'test_b方法名称的长度是：{_len}， 不等于4！')

