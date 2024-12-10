# # 1-misol
from decimal import Decimal


class ValueError(Exception):
    def __init__(self,message):
        self.message = message


class CheckValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if type(value) is Decimal:
            if -50 < value < 50:
                instance.__dict__[self.name]=value
            else:raise ValueError("Noto'gri qiymat")

        else:raise ValueError("Noto'gri qiymat")
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    def __delete__(self, instance):
        del instance.__dict__[self.name]

import random

class Temp:
    temp = CheckValue()
    def __init__(self,temp):
        self.temp = temp
        print(self.temperatura())

    def temperatura(self):
        aa = Decimal(random.uniform(-10,40))
        ii = aa.quantize(Decimal("1.0"))
        return ii

b = Decimal(input("Temperaturani kiriting: "))
a= Temp(b)





from decimal import Decimal


#-----------------------------------------------------------------------------
# # 2-misol
# from decimal import Decimal
#
#
# class ValueError(Exception):
#     def __init__(self,message):
#         self.message = message
#
#
# class CheckValue:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value):
#         if type(value) is Decimal:
#             if value < Decimal("1000000"):
#                 ii = input("Password: ")
#                 if ii == "12345":
#                     instance.__dict__[self.name]=value
#                 else:print("Sizdan bunday huquq yo'q")
#             else:raise ValueError("Hisobda maglag' yetarli emas!!")
#
#         else:raise ValueError("Noto'gri qiymat")
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
# import random
#
# class Bank:
#     yechish_mablagi = CheckValue()
#     def __init__(self,yechish_mablagi):
#         self.yechish_mablagi = yechish_mablagi
#         self.sana()
#
#     def sana(self):
#         c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
#         b = random.choice(c)
#         return b
#
#     def pulyechish(self):
#         return f"Hisobingizdan {self.yechish_mablagi} so'm yechildi ({self.sana()})"
#
#
#
#
# narx = Decimal(input("Qancha mablag' yechmoqchisiz: "))
# aa = Bank(narx)
# print(aa.pulyechish())

#-----------------------------------------------------------------------------
# 3-misol

# class ValueError(Exception):
#     def __init__(self,message):
#         self.message = message
#
# class CheckChipta:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value):
#         if type(value) is Decimal:
#             instance.__dict__[self.name]=value
#         else:raise ValueError("Qiymat noto'g'ri kiritildi")
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#
# class Chipta:
#     def __init__(self,tolov):
#         self.tolov = tolov
#         self.sana()
#         print(self.sotib_olish())
#
#     def sana(self):
#         import random
#         c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
#         b = random.choice(c)
#         return b
#
#     def sotib_olish(self):
#         return f"Chipta sotildi ({self.sana()})"
#
#
#
# aa = Decimal(input("Pulni kiriting: "))
# ii = Chipta(aa)


#-----------------------------------------------------------------------------
# 4-misol
#
# class ValueError(Exception):
#     def __init__(self,message):
#         self.message = message
#
#
# class CheckSalary:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value):
#         if type(value) == Decimal:
#             if value > 0:
#                 instance.__dict__[self.name] = value
#             else:raise ValueError("Qiymat notogri kiritildi!!")
#         else:
#             raise ValueError("Qiymat notogri kiritildi!!")
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#
#
# class Salary:
#     salary = CheckSalary()
#     def __init__(self,salary):
#         self.salry = salary
#         self.sana()
#         print(self.oylik())
#
#     def sana(self):
#         import random
#         c = ["2024.12.21", "2024.12.09", "2024.12.01", "2024.12.05"]
#         b = random.choice(c)
#         return b
#     def oylik(self):
#         return f"Sizning {self.salry} so'm oyligingiz o'tkazildi sana: {self.sana()}"
#
#
# aa = Decimal(input("Oylik maoshni kiriting: "))
# ii = Salary(aa)








































