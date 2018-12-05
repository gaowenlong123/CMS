#测试过程的 主入口
import sys
import unittest
sys.path.append("..")

from CMSTestServer.Base.Base_Unittest import ParametrizedTestCase
from datetime import datetime

#测试用例
from CMSTestRepository.TestCase.post import post


# 可以写成手动选的，通过gui，来选择要执行的脚本，当然可执行的脚本可以生成，都可以实现的
def MainRun():
    start_time = datetime.now()

    #运行登录，记录Cookie

    suite = unittest.TestSuite()

    suite.addTest(ParametrizedTestCase.parametrize(post))

    unittest.TextTestRunner(verbosity=1).run(suite)

    end_time = datetime.now()
    print('结束测试end')


if __name__ == '__main__':
    MainRun()

