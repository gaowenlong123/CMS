from CMSTestServer.Base.Base_Unittest import ParametrizedTestCase
from CMSTestServer.Supplement.Base_Yaml import getYaml
from CMSTestServer.Supplement.Base_Os import change_path
import sys
from CMSTestRepository.TestPage.publish_post_page import publish_post_page


class post(ParametrizedTestCase):
    def test_publish_post(self):
        app = {"logTest": self.logTest,
               "driver": self.driver,
               "test_msg": getYaml('E:\Pycharm_Git\CMS_TEST\CMSTestRepository\Yamls\Content_Management\post.yaml'),
               "caseName": sys._getframe().f_code.co_name}

        check_data=[]

        page=publish_post_page(app)
        page.operate()
        page.checkPoint(check_data)

    def test_two(self):
        pass

    @classmethod
    def setUpClass(cls):
        # 登录
        print('执行测试1')
        super(post, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        # 一个test结束运行
        print('结束测试2')
        super(post, cls).tearDownClass()
