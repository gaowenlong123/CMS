from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

class  Function():
    def __int__(self):
        pass

    def find_xpath(self ,driver ,xpath=''):
        return WebDriverWait(driver , 20).until(lambda  x : x.find_element_by_xpath(xpath))

    def find_id(self , driver , id =''):
        return WebDriverWait(driver , 20).until(lambda  x : x.find_element_by_id(id))


    def switch_window(self,driver, total=0, target=-1):  # 扩展装饰器 ,暂定两个页面的交互
        while True:
            if len(driver.window_handles) == total:
                self.handles = driver.window_handles
                break
        driver.switch_to.window(self.handles[-1])

    def refresh(self ,driver ,t):
        time.sleep(t)
        driver.refresh()

    def sleep(self ,t):
        time.sleep(t)
