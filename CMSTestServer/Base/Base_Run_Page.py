from CMSTestServer.Root.Base_Page import Base_Page_interface
from CMSTestServer.Supplement.Base_Error import get_error
from CMSTestServer.Base_Run_Operate import Operate_Elements
from CMSTestServer.Supplement.Base_Enum import Eunms as be


class Page_Objects(Base_Page_interface):

    def __init__(self,kwargs):

        self.driver = kwargs["driver"]

        self.operateElement = Operate_Elements(self.driver)  # 实例化操作对象,一个用例实例化一次

        if kwargs.get("launch", "0") == "0":  # 若为空， 刷新页面
            self.driver.get(self.driver.current_url)


        self.test_msg = kwargs["test_msg"]  # yaml 文件的数据
        # yaml信息拿进去
        self.testInfo = self.test_msg[1]["testinfo"]
        self.testCase = self.test_msg[1]["testcase"]
        self.test_check = self.test_msg[1]["check"]
        # 第一层传递的数据
        self.logTest = kwargs["logTest"]
        self.caseName = kwargs["caseName"]


        # 自定义，看需不需要

        self.isOperate = True

        self.get_value = []  # 测试的实际数据
        self.is_get = False  # 检查点特殊标志，结合get_value使用。若为真，说明检查点要对比历史数据和实际数据
        self.msg = ""

    '''
     操作步骤
    '''

    def operate(self):

        if self.test_msg[0] is False:
            self.isOperate = False
            return False

        # 操作testcase

        for item in self.testCase:
            result = self.operateElement.operate(item, self.testInfo, self.logTest)
            try:
                if not result["result"]:
                    msg = get_error({"type": be.DEFAULT_ERROR, "element_info": item["element_info"]})
                    print(msg)
                    self.testInfo[0]["msg"] = msg
                    self.isOperate = False
                    return False
                # if item.get("is_time", "0") != "0":  #=-=
                #     time.sleep(item["is_time"])  # 等待时间
                #     print("==等待%s秒==" % item["is_time"])  #=-=
                # if item.get("operate_type", "0") == op.get_value or item.get("operate_type", "0") == op.get_text:
                #     self.get_value.append(result["text"])
                #     self.is_get = True  # 对比数据
            except TypeError:
                print('error===> ', item['operate_type'], '  没有Return {}')

        return True

    # 检查执行
    def checkPoint(self, input_kwarg):
        result = self.check(input_kwarg)

        # statistics_result(result=result, testInfo=self.testInfo, caseName=self.caseName,
        #                   driver=self.driver, logTest=self.logTest,
        #                   testCase=self.testCase,
        #                   testCheck=self.test_check)

    '''
    检查点
    caseName:测试用例函数名 用作统计
    logTest： 日志记录
    '''

    def check(self, kwarg):
        ''' kwarg : 传入的对比数据 [] '''

        self.get_value=kwarg

        result = True
        # if kwargs.get("check_point", "0") != "0":      ?????
        #     return kwargs["check_point"]

        if self.isOperate:
            for item in self.test_check:

                resp = self.operateElement.operate(item, self.testInfo, self.logTest)
                # 默认检查点，就是查找页面元素，如果元素找不到就一定报错

                kwargs=item  #先留着看看

                if kwargs.get("check", be.DEFAULT_CHECK) == be.DEFAULT_CHECK and not resp["result"]:
                    m = get_error(
                        {"type": be.DEFAULT_CHECK, "element_info": item["element_info"], "info": item["info"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break

                # 历史数据和实际数据对比  ， 实际数据不在历史数据中，就是失败
                if kwargs.get("check", be.DEFAULT_CHECK) == be.COMPARE and self.is_get and resp["text"] \
                        not in self.get_value:  # 历史数据和实际数据对比
                    result = False
                    m = get_error({"type": be.COMPARE, "current": item["element_info"], "history": resp["text"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    break

                #  相反检查点，表示如果检查元素存在就说明失败，如  能在页面找到该元素，就是检查失败
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY and resp["result"]:
                    m = get_error({"type": be.CONTRARY, "element_info": item["element_info"], "info": item["info"]})
                    print(m)
                    self.testInfo[0]["msg"] = m  # 将错误信息加入到 testinfo 中
                    result = False
                    break
                # 检查点关键字contrary_getval: 相反值检查点，如果对比成功，说明失败
                if kwargs.get("check", be.DEFAULT_CHECK) == be.CONTRARY_COMPARE and self.is_get and resp["result"] \
                        in self.get_value:
                    m = get_error(
                        {"type": be.CONTRARY_COMPARE, "current": item["element_info"], "history": resp["text"]})
                    print(m)
                    self.testInfo[0]["msg"] = m
                    result = False
                    break

        else:
            result = False
        return result

