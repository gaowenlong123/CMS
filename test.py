# from selenium import webdriver
# from Base.str_enum import Eunms as enum
# # wd = webdriver.Chrome()
# # wd.get('Https://www.baidu..com')
#
# operate={'check_time':10 ,'find_type':'None'}
#
# t = operate['check_time'] if operate.get('check_time' , '0') !='0' else  enum.WAIT_TIME
# a =operate['find_type'] if operate['find_type'] != 'None' else None
#
# print(a)
# print(operate)
#
# b=[]
# a='1,2,34，2222'
# a1=a.split(',')
#
# for i in a1:
#     m=i.split('，')
#     print(m)
#     for i in m:
#         b.append(i)
# print(b)

# import sys
# sys.path.append("..")
# a=sys.path
# print(a)
#
# b=sys._getframe().f_code.co_name
# print(b)

# from Base.BaseYaml import  getYaml
# import os
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__), p)
# )
# a=PATH("./Yamls/Config.yaml")
# print(a)
# openurl = getYaml(a)
# print(openurl[1]['url'])


# from selenium import webdriver
# w=webdriver.Chrome()
# w.get('https://cmstest02.36kr.com')
# w.implicitly_wait(10)
# w.find_element_by_xpath('//*[@id="app"]/div/div/span[2]/a').click()
# w.find_element_by_xpath()
# w.find_element_by_xpath().submit()
# w.current_window_handle
# print(a)


# import os
# str=''
# count=0
# print(os.path.abspath(os.path.dirname(__file__)))
# a=os.path.dirname(__file__).split('/')
# print('aa',a)
#
#
# path="../Yamls/test/test1.yaml"
# back_num=len(path.split('/')[0])
# print(back_num)



from CMSTestServer.Supplement.Base_pickle import *
from selenium import webdriver
import time



# 读本地缓存写入
dict=read_pickle('Cookie.pickle')
print(dict)
w=webdriver.Chrome()
w.get('http://cmstest02.36kr.com')
#写入
for i in dict:
    cookie=dict[i]
    print(cookie)
    w.add_cookie(cookie)

time.sleep(3)
w.refresh()




#  写入
# w=webdriver.Chrome()
# w.get('http://cmstest02.36kr.com')
# input('dada')  #登录操作
# a=w.get_cookies()
# dict={}
# count=0
# for i in a:
#     dict.update({str(count):i})
#     count+=1
# print(dict)
#
# writeInfo(dict , path='Cookie.pickle')