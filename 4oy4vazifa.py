# class Lower:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __set__(self, instance, value:str):
#          value = value.lower()
import math
from logging import exception


# ----------------------------------------------------------------
# 2-misol
class ValueError(Exception):
    def __init__(self,message):
        self.message = message



class Plus:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.name]=value
        else: raise ValueError("Qiymat xato kiritilgan!!")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# class AA:
#     son = Plus()
#     def __init__(self,son):
#         self.son = son
#
#
#
# a=AA(-8)
#

# ----------------------------------------------------------------
#3-misol
from datetime import datetime, timedelta
#
# a = datetime.now()
# c = a - timedelta(days=7)
# d = a + timedelta(days=7)
# print(f"Bugungi sana {a}")
# print(f"7 kun oldingi sana {c}")
# print(f"7 kun keyingi sana {d}")


# ----------------------------------------------------------------
#4-misol
# from datetime import datetime
# ii = input("Tug'ilgan sanangizni kiriting(YYYY-MM-DD): ")
# s = datetime.strptime(ii,"%Y-%m-%d")
# dd = datetime.now()
# if s == dd:
#     print("🥳🥳🥳Tug'ilgan kuningiz bilan🥳🥳🥳")
# else:
#     print("Sizning yoshingiz",(dd-s)//365)


# ----------------------------------------------------------------
# 5-misol
from datetime import datetime
# v1 = input("Birinchi sanani kiriting(YYYY-MM-DD): ")
# v2 = input("Ikkinchi sanani kiriting(YYYY-MM-DD): ")
# vaqt1 = datetime.strptime(v1, "%Y-%m-%d" )
# vaqt2 = datetime.strptime(v2, "%Y-%m-%d")
#
# soniyalar = abs((vaqt1-vaqt2).total_seconds())
# print(f"Sanalar orasidagi soniyalar farqi {int(soniyalar)}")

# ----------------------------------------------------------------
#
# 6-misol
# a = input("Aylana radiusini kiriting: ")
# if a.isdigit():
#     a = int(a)
#     print(math.pi*a**2)
#
# ----------------------------------------------------------------
# 7-misol
# class Manfiy(Exception):
#     def __init__(self,message):
#         self.message = message
# a = int(input("Son: "))
# if a > 0:
#     print(f"Kvadrat ildizdan {math.sqrt(a)}")
#     print(f"Kub ildizdan {math.pow(a,1/3)}")
#
# else:raise Manfiy("Iltimos musbat son kirting")


# ----------------------------------------------------------------
# 8-misol
# import random
# x =[]
# for i in range(5):
#     a = random.randint(1,100)
#     x.append(a)
# print(x)

###bb
# import random
# for i in range(3):
#     x=random.random()
#     print(x)

####ccc
# aa = [1,2,3,4,5,6,7,8]
# a = sum(aa)
# print(a)













