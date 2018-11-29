#抽象类加抽象方法就等于面向对象编程中的接口
from abc import ABCMeta,abstractmethod

class Base_Page_interface(object):
    __metaclass__ = ABCMeta  # 指定这是一个抽象类

    @abstractmethod  # 抽象方法
    def operate(self):
        pass

    @abstractmethod
    def checkPoint(self , kwarg):
        pass

