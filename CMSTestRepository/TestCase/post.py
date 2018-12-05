from CMSTestServer.Base.Base_Unittest import ParametrizedTestCase
from CMSTestServer.Supplement.Base_Yaml import getYaml
from CMSTestServer.Supplement.Base_Os import change_path
import sys
from CMSTestRepository.TestPage.publish_post_page import publish_post_page


class post(ParametrizedTestCase):

    def test_publish_post(self):
        app = {"logTest": self.logTest,
               "driver": self.driver,
               "test_msg": getYaml('E:\Pycharm_Git\CMS\CMSTestRepository\Yamls\Content_Management\post.yaml'),
               "caseName": sys._getframe().f_code.co_name}

        check_data=[]

        page=publish_post_page(app)
        page.operate()
        page.checkPoint(check_data)

    def test_two(self):
        app = {"logTest": self.logTest,
               "driver": self.driver,
               "test_msg": getYaml('E:\Pycharm_Git\CMS\CMSTestRepository\Yamls\Content_Management\post.yaml'),
               "caseName": sys._getframe().f_code.co_name}

        check_data = []

        page = publish_post_page(app)
        page.operate()
        page.checkPoint(check_data)

    @classmethod
    def setUpClass(cls):

        print('开始执行用例测试 - 实例')
        super(post, cls).setUpClass()

    def setUp(self):
        print('一个用例单个方法的开始  - 实例')
        self.get_driver()                  #启动浏览器
        super().setUp()

    def tearDown(self):
        print('一个用例单个方法的结束  - 实例')
        super().tearDown()                        #每次测试都关闭浏览器 ,不写就不关闭
        import time
        time.sleep(2)
        self.driver.close()
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # 一个test结束运行
        print('结束测试 - 实例')
        super(post, cls).tearDownClass()
