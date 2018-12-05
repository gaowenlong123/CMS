import re
from CMSTestServer.Base_Element import Element
from selenium.webdriver.common.action_chains import *
from CMSTestServer.Supplement.Base_Enum import find_type as f


class Operate_Fun():

    def __init__(self , webdriver):
        self.wd = webdriver
        self.handles = []
        self.element=Element(self.wd)
        pass


    def get_object(self, operate):   #还没用
        # 有的时候，我会获得元素对象，再通过他获得接下来的元素
        my_object = self.element.Element_By(operate)
        self.element.set_object(object=my_object,isObject=True)

    def get_driver(self):   #切换到diver ，不用object
        self.element.set_object()


    def click(self, operate):
        # 下拉框元素我不会通过Id来拿
        # 若果1是数字，就是list，如果是元素就点击一次
        # 如果是driver点击还是元素对象下的点击

        #   数字表示要点击的元素列表,
        '''必须是数字,从零开始，兼容中英大小写'''
        if ',' in operate['element_info'] or '，' in operate['element_info']:
            temp_list = []
            temp = operate['element_info'].split(',')
            for str in temp:
                i = str.split('，')
                for m in i:
                    temp_list.append(m)
            # temp_list=sorted(temp_list)

            if self.element.object == False:
                self.element.Element_By(operate).click()
            else:
                print("点击元素对象下的值")
                for m in temp_list:
                    self.element.Element_By_object(operate)[m].click()
                    time.sleep(0.5)
            return {'result': True}
        else:
            if self.element.is_object == False:
                self.element.Element_By(operate).click()
            else:
                print("点击元素对象下的值")
                self.element.Element_By_object(operate).click()
            return {'result': True}

    def send_keys(self, operate):
        temp = self.element.Element_By(operate)
        temp.send_keys('.')
        temp.clear()
        temp.send_keys(operate['info'])  # 'msg' ????
        return {'result': True}

    def get_text(self, operate):  # =-=
        if operate.get("find_type") == f.find_elements_by_id:
            element_info = self.element.Element_By(operate)[operate["index"]]

            result = element_info.get_attribute("text")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.element.Element_By(operate)
        result = element_info.text
        # result = element_info.get_attribute("text")  #===>None

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # ===> [音,频,小,管,家]
        return {"result": True, "text": "".join(re_reulst)}
        pass

    def get_value(self, operate):  # =-= ???
        if operate.get("find_type") == f.find_elements_by_id:
            element_info = self.element.Element_By(operate)[operate["index"]]

            result = element_info.get_attribute("value")
            re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)  # 只匹配中文，大小写，字母
            return {"result": True, "text": "".join(re_reulst)}

        element_info = self.element.Element_By(operate)
        result = element_info.get_attribute("value")

        re_reulst = re.findall(r'[a-zA-Z\d+\u4e00-\u9fa5]', result)
        return {"result": True, "text": "".join(re_reulst)}
        pass

    def move_to_element(self, operate):  # =-=
        ActionChains(self.wd).move_to_element(self.element.Element_By(operate)).perform()
        return {"result": True}
        pass

    def get_list(self, operate):
        # 下拉框元素我只会用Xpath来拿
        print(" get_list 只用 xpth")
        if operate['find_type'] == f.find_elements_by_xpath:
            pass
        pass


    #不操作元素
    def switch_window(self, operate, total=0, target=-1):  # 扩展装饰器 ,暂定两个页面的交互
        while True:
            if len(self.wd.window_handles) == int(operate['info']):
                self.handles = self.wd.window_handles
                break
        self.wd.switch_to.window(self.handles[-1])
        return {'result': True}

    def sleep(self, operate):
        import time
        time.sleep(operate['info'])
        return {'result': True}

    def close_window(self, operate):
        # 能不能先切换窗口，再关之前那个窗口
        print('aaaa', self.wd.current_window_handle)
        time.sleep(10)
        self.wd.close()
        self.handles = self.wd.window_handles
        print(self.handles)
        print(self.wd.current_window_handle)
        self.wd.switch_to(self.handles[operate['info']])
        return {'result': True}
        pass

    def scroll_down(self, operate):
        pass

    def scroll_up(self, operate):
        pass

    def refresh(self, operate):
        time.sleep(operate['info'])
        self.wd.refresh()
        return {'result': True}

    def change_size(self, operate):
        pass



