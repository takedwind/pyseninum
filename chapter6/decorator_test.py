import unittest
from .decorators import depend


class TestA(unittest.TestCase):

    def test_a(self):
        print(self.test_a.__name__)
        assert False

    def test_b(self):
        print(self.test_b.__name__)
        assert 1 == 0

    @depend('test_d')
    def test_c(self):
        print(self.test_c.__name__)
        assert 1


# @depend('test_a')
class TestB(unittest.TestCase):

    # @depend('test_a')
    def test_d(self):
        print(self.test_d.__name__)
        assert False


if __name__ == '__main__':
    unittest.main(verbosity=2)
