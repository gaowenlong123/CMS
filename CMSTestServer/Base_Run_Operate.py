from CMSTestServer.Base_Element import Element
import selenium.common.exceptions
from CMSTestServer.Base_Run_OperateFun import Operate_Fun
from CMSTestServer.Supplement.Base_Enum import Eunms as enum , operate_type as op


class Operate_Elements():
    '''  实例时需要传入webdriver '''
    def __init__(self ,webdriver):
        self.wd = webdriver

        self.element=Element(self.wd)     #一个测试用例，实例化一次
        self.OF=Operate_Fun(self.wd)


    #操作
    def operate(self , operate, testInfo, logTest):

        #找元素的时候可能是driver，也可能是根据对象来找！！！！！！！！！！！
        result = self.element.Find_Element(operate )

        if result['result']:   #如果找到元素，就执行
            return  self.operate_by(operate, testInfo, logTest)
        else:
            return result



    # 找到元素就执行
    def operate_by(self , operate, testInfo, logTest):
        try:
             #操作元素
            if self.element.is_Element(operate) != None:
                info = '%s _ %s _ %s _ %s'%(
                    operate.get('element_info' , ' '),operate.get('find_type' , ' ')
                    ,operate.get('operate_type' ,' '),operate.get('info',' ')
                )

                # logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志

                if operate.get('operate_type' , '0') =='0':
                    return {'result' : False}

                operate_E_fun={
                    op.click:lambda  :self.OF.click(operate),
                    op.send_keys:lambda  :self.OF.send_keys(operate),
                    op.get_text:lambda   :self.OF.get_text(operate),
                    op.get_value:lambda  :self.OF.get_value(operate),
                    op.move_to_elemrnt:lambda   :self.OF.move_to_element(operate),
                    op.get_list : lambda   : self.OF.get_list(operate)
                }
                return operate_E_fun[operate['operate_type']]()

            #不操作元素
            else:
                info = '%s _ %s _ %s' % (
                    operate.get('element_info', ' ')
                    , operate.get('operate_type', ' '), operate.get('info', ' ')
                )

                #logTest.buildStartLine(testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + info)  # 记录日志
                operate_fun={
                    op.switch_window:lambda  : self.OF.switch_window(operate),
                    op.scroll_down: lambda  :self.OF.scroll_down(operate),
                    op.scroll_up: lambda  :self.OF.scroll_up(operate),
                    op.close_window: lambda  :self.OF.close_window(operate),
                    op.change_size: lambda  :self.OF.change_size(operate),
                    op.get_driver:lambda  :self.OF.get_driver(),
                    op.sleep :lambda  :self.OF.sleep(operate),
                    op.refresh : lambda :self.OF.refresh(operate)
                }
                return operate_fun[operate['operate_type']]()



         # =-=
        except IndexError:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate["element_info"] + "索引错误")  # 记录日志
            # print(operate["element_info"] + "索引错误")
            return {"result": False, "type": enum.INDEX_ERROR}
        except selenium.common.exceptions.NoSuchElementException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素不存在或没加载完成")  # 记录日志
            # print(operate["element_info"] + "页面元素不存在或没有加载完成")
            return {"result": False, "type": enum.NO_SUCH}
        except selenium.common.exceptions.StaleElementReferenceException:
            logTest.buildStartLine(
                testInfo[0]["id"] + "_" + testInfo[0]["title"] + "_" + operate[
                    "element_info"] + "页面元素已经变化")  # 记录日志
            # print(operate["element_info"] + "页面元素已经变化")
            return {"result": False, "type": enum.STALE_ELEMENT_REFERENCE_EXCEPTION}
        except KeyError:
            # 如果key不存在，一般都是在自定义的page页面去处理了，这里直接返回为真
            return {"result": True}