from chapter6.logs import log
import unittest


def func_a(*args, **kwargs):
    log.debug(func_a.__name__, extra={'status': 'running'})

    return 1 / args.__len__(), 1 / kwargs.__len__()


# func_a(1, name='json')


class TestA(unittest.TestCase):

    def test_a(self):
        log.debug(self.test_a.__name__, extra={'status': 'running'})
        assert True

    def test_b(self):
        log.debug(self.test_b.__name__, extra={'status': 'running'})
        assert True


if __name__ == '__main__':
    unittest.main()
