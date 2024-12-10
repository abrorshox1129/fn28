# #importlar
# import module_1
# import module_2
# import module_3
#
#
# print(module_1.str1)
# print(module_1.start())
# print(module_2.str1)
# print(module_2.start())
# print(module_3.str1)
# print(module_3.start())
#
#
# from module_1 import *
# print(str1)
# print(start())
#
#
# from module_1 import str1 as module_1_str1 , start
# from module_2 import str1,start as module2_start
# print(start())
# print(module2_start())
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetr(self):
        pass

class Triangle(Shape):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return self.a * self.b

    def perimetr(self):
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b


    def area(self):
        return self.a * self.b

    def perimetr(self):
        return (self.a+self.b)*2



t = Triangle(1,2,3)
print(t.area())


s = Square(2,4)
print(s.area())











