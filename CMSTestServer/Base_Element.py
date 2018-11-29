from CMSTestServer.Supplement.Base_Enum import Eunms as enum , find_type as f
from  selenium.webdriver.support.ui import WebDriverWait
import selenium.common.exceptions

class Element():
    def __init__(self,wd):   #什么时候初始化
        self.wd=wd
        self.object=None #等到object传递进来，操作完元素要把object为空
        self.is_object=False
        pass

    #先检查元素是否存在
    def Find_Element(self ,operate):
        '''  执行testcase '''

        #如果没有检查时间，t 就为else 后面的值  , 并且字典不新增加值 。如果有，t 就是检查时间
        t = operate['check_time'] if operate.get('check_time' , '0') !='0' else  enum.WAIT_TIME

        try:
            if type(operate)==list:
                #多个操作
                for item in operate:
                    t = item['check_time'] if item.get('check_time' , '0') !='0' else  enum.WAIT_TIME
                    if self.is_Element(item) == None:  #操作不需要查询元素
                        return {'result': True}

                    if self.is_object == False:
                        WebDriverWait(self.wd , t).until(lambda b :  self.Element_By(item))
                    else:
                        WebDriverWait(self.wd, t).until(lambda b: self.Element_By_object(item))
                    return  {'result':True}          #不需要返回list吗？ 只是检查元素

            if type(operate)==dict:
                #单个操作
                if self.is_Element(operate) == None:  # 操作不需要查询元素
                    return {'result': True}

                if self.is_object == False:
                    WebDriverWait(self.wd, t).until(lambda b: self.Element_By(operate))
                else:
                    WebDriverWait(self.wd, t).until(lambda b : self.Element_By_object(operate))
                return {'result': True}

        #报错直接提示
        except selenium.common.exceptions.NoSuchElementException:
            print('BaseOperate__error===> 没用该元素')
        except selenium.common.exceptions.TimeoutException:
            print('BaseOperate__error===> 等待时间超时')
        except selenium.common.exceptions.WebDriverException:
            print('BaseOperate__error===> Webdriver出现问题')

    def set_object(self, object=None, isObject=False):
        '''   默认清空 object'''
        self.object = object
        self.is_object = isObject

    def Element_By(self ,element_dic):

        ''' lamda :  '''
        print(element_dic['element_info'])
        find = {  # 不需要变量,因为后面不需要
            f.find_element_by_id: lambda: self.wd.find_element_by_id(element_dic['element_info']),
            f.find_element_by_xpath: lambda: self.wd.find_element_by_xpath(element_dic['element_info']),
            f.find_element_by_class_name: lambda: self.wd.find_element_by_class_name(element_dic['element_info']),
            f.find_element_by_tag_name: lambda: self.wd.find_element_by_tag_name(element_dic['element_info']),
            f.find_element_by_link_text: lambda: self.wd.find_element_by_link_text(element_dic['element_info']),

            f.find_elements_by_id: lambda: self.wd.find_elements_by_id(element_dic['element_info']),
            f.find_elements_by_xpath: lambda: self.wd.find_elements_by_xpath(element_dic['element_info']),
            f.find_elements_by_class_name: lambda: self.wd.find_elements_by_class_name(element_dic['element_info']),
            f.find_elements_by_tag_name: lambda: self.wd.find_elements_by_tag_name(element_dic['element_info']),
            f.find_elements_by_link_text: lambda: self.wd.find_elements_by_link_text(element_dic['element_info']),
        }

        return find[element_dic['find_type']]()

    def Element_By_object(self, element_dic):

        ''' lamda :  '''
        find = {
            f.find_element_by_id: lambda : self.object.find_element_by_id(element_dic['element_info']),
            f.find_element_by_xpath: lambda : self.object.find_element_by_xpath(element_dic['element_info']),
            f.find_element_by_class_name: lambda : self.object.find_element_by_class_name(element_dic['element_info']),
            f.find_element_by_tag_name: lambda : self.object.find_element_by_tag_name(element_dic['element_info']),
            f.find_element_by_link_text: lambda : self.object.find_element_by_link_text(element_dic['element_info']),

            f.find_elements_by_id: lambda : self.object.find_elements_by_id(element_dic['element_info']),
            f.find_elements_by_xpath: lambda : self.object.find_elements_by_xpath(element_dic['element_info']),
            f.find_elements_by_class_name: lambda : self.object.find_elements_by_class_name(element_dic['element_info']),
            f.find_elements_by_tag_name: lambda : self.object.find_elements_by_tag_name(element_dic['element_info']),
            f.find_elements_by_link_text: lambda : self.object.find_elements_by_link_text(element_dic['element_info']),
        }

        return find[element_dic['find_type']]()

    def is_Element(self ,operate):
                                          #取不到返回，后面的值
        return operate['find_type'] if operate['find_type'] != 'None' else None


