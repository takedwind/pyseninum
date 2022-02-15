# 测试套件 —— 包含待测的模块、类、测试方
# 测试加载器 —— 决定测试模块、测试类、测试方法的加载
# 测试运行器 —— 记录测试过程、输出测试结果

# 测试结果输出到文本中——文本报告
# 测试结果输出到网页中——网页报告

from os.path import join, dirname
import unittest
# from chapter4.case import tests
from setting import SUIT_MODULE_1
from HTMLTestRunner import HTMLTestRunner

CASE_PATH = join(dirname(__file__), './chapter4/case')

# 测试套件初始化，测试加载器初始化
suit = unittest.TestSuite()
loader = unittest.defaultTestLoader
# loader = unittest.TestLoader()

# 测试加载器发现测试对象
for test in SUIT_MODULE_1:
    test_suit = loader.discover(start_dir=CASE_PATH, pattern=test)

# 测试对象加入测试套件
    suit.addTest(test_suit)

# 测试运行器初始化
# with open('./report.txt', 'w') as fp:
#     runner = unittest.TextTestRunner(fp, verbosity=2)
#
# # 运行测试
#     runner.run(suit)

with open('./report.html', 'wb') as fp:
    runner = HTMLTestRunner(fp, verbosity=2)
    runner.run(suit)


from chapter7.mail import email
email.send()
