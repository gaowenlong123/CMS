from CMSTestServer.Base.Base_Run_Page import Page_Objects


class publish_post_page(Page_Objects):
    def __init__(self, param , methodName='Page'):
        super(publish_post_page, self).__init__(param)

    def operate(self):
        print("可以执行我，大哥")
        super().operate()
        pass

    # def check(self, kwargs):
    #     pass