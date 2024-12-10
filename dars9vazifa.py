from mathematics import*
#
# num =1234567890987
# yigindi(num)
#
# 2-misol

# sec = 91000
# solution = sekund(sec)
# print(solution)

#
#3
# from figure import circle_perimetr
# from figure.square import square_area
# from figure.triangle import triangle_perimetr
#
# a = circle_perimetr(3)
# print(a)
#
# from figure import triangle
# a = 1
# b = 2
# c = 3
# print(triangle_perimetr(a,b,c))
#
# from figure import square
# a=4
# print(square_area(a))


from abc import abstractmethod

#4misol
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#
# class Car(Vehicle):
#     def start(self):
#          return "START tugmasi yordamida mashinani ishga tushuriladi"
#
#     def stop(self):
#         return "STOP tugmasi yordamida mashinani o'chirish mumkin"
#
#
# class Bicycle(Vehicle):
#     def start(self):
#         return "|ON| tugmasi orqali maxsus qurilmalarni ishga tushirasiz"
#
#     def stop(self):
#         return "|OFF| tugmasi orqali o'chirasiz"
#
#
#
#
# aa = Bicycle()
# print(aa.stop())
# print(aa.start())
#
#
# bb = Car()
# print(bb.start())
# print(bb.stop())
# from abc import ABC,abstractmethod
#

#5misol

# class Hayvonlar_ovozi(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
# class Dog(Hayvonlar_ovozi):
#     def make_sound(self):
#         return "wow wow"
#
# class Cat(Hayvonlar_ovozi):
#     def make_sound(self):
#         return "meow meow"
#
# class Cow(Hayvonlar_ovozi):
#     def make_sound(self):
#         return "Moo moo"
#
#
# p = Cow()
# print(p.make_sound())

#6 misol
# from abc import ABC,abstractmethod
# class Payment(ABC):
#     def process_payment(self):
#         pass
#
#
# class CreditCardPayment(Payment):
#     def process_payment(self,amount):
#         return f"{amount} summasi kredit karta orqali to'lash amalga oshirildi"
#
# class CryptoPayment(Payment):
#     def process_payment(self,amount):
#         return f"{amount} summasi kripto valyuta orqali to'landi"
#
#
# a = CreditCardPayment()
# print(a.process_payment(1000))


























