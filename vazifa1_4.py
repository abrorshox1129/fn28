# #1-misol
#
# class MyValueError(Exception):
#     def __init__(self,message):
#         self.message = message
#
#
# class CheckAge:
#     def __set_name__(self, owner, name):
#         self.yosh = name
#
#
#     def __set__(self, instance, value:int):
#         if value > 0:
#             instance.__dict__[self.yosh]=value
#
#         else:
#             raise MyValueError("Yosh musbat son bo'lishi kerak")
from requests.packages import imported_mod


#     def __get__(self, instance, owner):
#         return instance.__dict__[self.yosh]
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.yosh]
#
#
# class Age:
#     age = CheckAge()
#     def __init__(self,age):
#         self.age = age

# a = Age(33)


#2-misol
# class MyInvalidPhoneNumberError(Exception):
#     def __init__(self,message):
#         self.message = message
#
#
#
#
#
# class Checkphonenumber:
#     def __set_name__(self, owner, name):
#         self.item = name
#     def __set__(self, instance, value:str):
#         if value.startswith("+"):
#              if value[1:].isdigit():
#                  if len(value) == 13:
#                     instance.__dict__[self.item]=value
#
#              else:
#                  raise MyInvalidPhoneNumberError("raqam berilgan standartlarga javob bermaydi")
#
#         else:
#             raise MyInvalidPhoneNumberError("raqam berilgan standartlarga javob bermaydi")
#
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.item]
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.item]
#
# class PhoneNumber:
#     phonenumber = Checkphonenumber()
#     def __init__(self,phonenumber):
#         self.phonenumber=phonenumber
#
#
#
#
# a = PhoneNumber("+998903661016")



#3-misol
class MyWeakPasswordError(Exception):
    def __init__(self,message):
        self.message = message


class CheckPassword:
    def __set_name__(self, owner, name):
        self.password = name

    def __set__(self, instance, value:str):
        if len(value)>7:
            if "?"  in value:
                for i in value:
                    if i.isupper():
                        instance.__dict__[self.password]=value
                    else:
                        continue
            else:raise MyWeakPasswordError("Parol xato")
        else:raise MyWeakPasswordError("Parol xato")

    def __get__(self, instance, owner):
        return instance.__dict__[self.password]

    def __delete__(self, instance):
        del instance.__dict__[self.password]


class Password:
    password = CheckPassword()
    def __init__(self,password):
        self.password = password

v = Password("1111888?66")


#4-misol

class MyInvalidEmailError (Exception):
    def __init__(self,message):
        self.message = message

class CheckEmail:
    def __set_name__(self, owner, name):
        self.email = name

    def __set__(self, instance, value):
        if "@" in value:
            if "." in value:
                instance.__dict__[self.email] = value
            else:raise MyInvalidEmailError("Email xato kiritildi")
        else:raise MyInvalidEmailError("Email xato kiritildi")

    def __get__(self, instance, owner):
        return instance.__dict__[self.email]
    def __delete__(self, instance):
        del instance.__dict__[self.email]


class Email:
    email = CheckEmail()
    def __init__(self,email):
        self.email = email



# aa = Email("abror@gmail.com")


#5-misol

class MyUnderageError (Exception):
    def __init__(self,message):
        self.message = message

class CheckAge:
    def __set_name__(self, owner, name):
        self.age = name

    def __set__(self, instance, value):
        if value >= 16:
            instance.__dict__[self.age]=value

        else:raise MyUnderageError("Sizning yoshingiz kichik!!!")

    def __get__(self, instance, owner):
        return instance.__dict__[self.age]
    def __delete__(self, instance):
        del instance.__dict__[self.age]


class Age:
    age = CheckAge()
    def __init__(self,age):
        self.age = age


# a = Age(15)


#6-misol

class MyNegativePriceError (Exception):
    def __init__(self,message):
        self.message = message

class CheckPrice:
    def __set_name__(self, owner, name):
        self.price = name

    def __set__(self, instance, value):
        if 0<=value:
            instance.__dict__[self.price]=value
        else:raise MyNegativePriceError("Qiymat manfiy bolmasligi zarur!!")

    def __get__(self, instance, owner):
        return instance.__dict__[self.price]
    def __delete__(self, instance):
        del instance.__dict__[self.price]


class Price:
    price = CheckPrice()
    def __init__(self,price):
        self.price = price



# sum = Price(12)


#7-misol
class MyInvalidGradeError(Exception):
    def __init__(self,message):
        self.message = message


class CheckGrade:
    def __set_name__(self, owner, name):
        self.grade = name


    def __set__(self, instance, value):
        if 0 < value < 13:
            instance.__dict__[self.grade]=value

        else:raise MyInvalidGradeError("Qiymat 1 va 12 sonlari orasida bo'lishi kerak")

    def __get__(self, instance, owner):
        return instance.__dict__[self.grade]
    def __delete__(self, instance):
        del instance.__dict__[self.grade]



class Grade:
    grade = CheckGrade()
    def __init__(self,grade):
        self.grade = grade




# ss = Grade(12)



#8-misol

class MyInvalidDateError (Exception):
    def __init__(self,message):
        self.message = message

class CheckDate:
    def __set_name__(self, owner, name):
        self.date = name

    def __set__(self, instance, value):
        if 1000 <= value <= 9999:
            instance.__dict__[self.date] = value
        else: raise MyInvalidDateError("Yil xato kiritildi")

    def __get__(self, instance, owner):
        return instance.__dict__[self.date]

    def __delete__(self, instance):
        del instance.__dict__[self.date]


class Checkmonth:

    def __set_name__(self, owner, name):
        self.date = name

    def __set__(self, instance, value):
        if 1<=value<=12:
            instance.__dict__[self.date] = value
        else:
            raise MyInvalidDateError("Oy xato kiritildi")

    def __get__(self, instance, owner):
        return instance.__dict__[self.date]

    def __delete__(self, instance):
        del instance.__dict__[self.date]

class Checkday:
    def __set_name__(self, owner, name):
        self.date = name

    def __set__(self, instance, value):
        if 1<=value<=31:
            instance.__dict__[self.date] = value
        else:
            raise MyInvalidDateError("Kun xato kiritildi")

    def __get__(self, instance, owner):
        return instance.__dict__[self.date]

    def __delete__(self, instance):
        del instance.__dict__[self.date]


class DAte:
    date = CheckDate()
    month = Checkmonth()
    day = Checkday()
    def __init__(self,date,month,day):
        self.date = date
        self.month = month
        self.day = day



aa = DAte(1000,12,31)