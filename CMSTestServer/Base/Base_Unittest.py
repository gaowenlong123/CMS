import unittest
from selenium import webdriver
import os
from CMSTestServer.Supplement.Base_Yaml import getYaml
from CMSTestServer.Base.Base_Log import myLog
from CMSTestServer.Supplement.Base_pickle import *
from CMSTestServer.Supplement.Base_Func import Function



class ParametrizedTestCase(unittest.TestCase):

    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param=param

    @classmethod
    def setUpClass(cls):
        # 登录
        print('开始执行用例测试 - 父类')
        # cls.driver = get_driver()
        cls.logTest =None
        # cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器


    def setUp(self):
        print('一个用例单个方法的开始  - 父例')
        pass


    def tearDown(self):
        print('一个用例单个方法的结束  - 父例')

    @classmethod
    def tearDownClass(cls):
        print('结束测试 - 父类')
        pass



    @staticmethod
    def parametrize(testcase_klass, param=None):
        # print("---parametrize-----")
        # 先添加测试用例，再执行
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite


    def get_driver(self):
        # chromedriver = PATH("../exe/chromedriver.exe")  #暂不添加吧
        # os.environ["webdriver.chrome.driver"] = chromedriver  #添加环境变量     (有其他更好的方法）
        # driver = webdriver.Chrome(chromedriver)
        print("WMWMWMWMWMWMWMWMWMWMWMWMWMWWWMWMWMWWMWMWMWMWMWWMWMW")
        self.path='E:\Pycharm_Git\CMS\CMSTestServer\Base\Cookie.pickle'

        #可以参数化
        Cookie_dict = read_pickle(self.path)
        user = {'account': '23322228888', 'pass': 'er2222', 'name': '自动化小能手'}


        self.driver = webdriver.Chrome()
        print(self.driver.get_cookies())
        self.driver.maximize_window()  # 将浏览器最大化
        openurl = getYaml('E:\Pycharm_Git\CMS\CMSTestRepository\Yamls\Config.yaml')[1]['url']
        self.driver.get(openurl)

        for i in Cookie_dict:
            cookie = Cookie_dict[i]
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        self.driver.implicitly_wait(10)

        self.Func = Function()
        if self._check_ReLogin(user):
            print('重新登录')
            # driver.close()
            # driver.quit()
            self._login(user)  #重新登录，应该一下就可以成功

        # return self.driver  # 返回一个webdrier


    def _login(self,user):
        #登录操作
        self.driver.get(getYaml('E:\Pycharm_Git\CMS\CMSTestRepository\Yamls\Config.yaml')[1]['url'])
        # driver.maximize_window()

        self.Func.find_xpath(self.driver, xpath='//*[@id="app"]/div/div/span[2]/a').click()
        self.Func.switch_window(self.driver, 2)
        self.Func.find_xpath(self.driver, xpath='//*[@id="kr-shield-username"]').send_keys(user['account'])
        self.Func.find_xpath(self.driver, xpath='//*[@id="kr-shield-password"]').send_keys(user['pass'])
        self.Func.find_xpath(self.driver, xpath='//*[@id="kr-shield-submit"]').click()

        try:
            self.Func.sleep(3)
            self.Func.switch_window(self.driver,1)
            self.Func.refresh(self.driver,0)
            # self.Func.find_xpath(driver, xpath='//*[@id="2$Menu"]/li[1]/a').click()

        #写进文件中
            list = self.driver.get_cookies()
            dict={}
            count=0
            for i in list:
                dict.update({str(count):i})
                count+=1
            print(dict)
            writeInfo(dict , path=self.path)
        except:
            print('请手动输入Cookie')


    def _check_ReLogin(self ,user):
        #检查失败 返回true
        try:
            page_name = self.Func.find_xpath(self.driver, xpath='//*[@id="app"]/div/div[1]/div/div[1]/span/span[1]')

            print('username = ', page_name.text)  # 登录验证
            if page_name.text != user['name']:
                self.Func.sleep(3)
                print('username again = ', page_name.text)  # 登录验证
                if page_name.text != user['name']:
                    return True
                # 如果还是不为用户名，就重新登录一遍
            return False
        except:
            print('检查不通过')
            return True







