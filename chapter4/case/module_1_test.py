import unittest
from unittest import skip, skipIf, skipUnless
from os import name
from sys import version_info, platform


# @skip
class A(unittest.TestCase):

    def test_a1(self):
        self.assertEqual(1, 1)

    @skip
    def test_a2(self):
        ...


@skipIf(name != 'nt', '')
class B(unittest.TestCase):

    @skipIf(version_info[0] < 3, '')
    def test_b1(self):
        ...

    @skipUnless('win' in platform, '')
    def test_b2(self):
        ...
