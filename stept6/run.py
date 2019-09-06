#  测试报告方式运行
import time
import unittest


# 也可以把报告模块放到具体的python安装目录下面的lib文件夹里面
from HTMLTestReportCN import HTMLTestRunner

# 生成一个测试包的路径
dirpath = './scripts'

# 生成discover对象
discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')

currenttime = time.strftime('%y%m%d%H%M%S')

# 通过字符串拼接生成一个测试路径
filedir = './Reports/' + 'report' + currenttime + '.html'


# w wb(以二进制的方式清空在写入)
fp = open(filedir, 'wb')


# # 生成一个执行对象(使用Lib的内置库)
runner = HTMLTestRunner(stream=fp,
                        title='计算器自动化测试报告',
                        description='计算器自动化测试项目详细描述',
                        tester="我是你爸爸")

# 执行测试对象
runner.run(discover)

# 关闭文本
fp.close()
