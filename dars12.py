# class Book:
#     def __init__(self,kitob,muallifi,sahifalri):
#         self.kitob = kitob
#         self.muallifi = muallifi
#         self.sahifalr = sahifalri
#
# books = []
# class Library(Book):
#     def __init__(self,kitob,muallifi,sahifalari):
#         super().__init__(kitob,muallifi,sahifalari)
#
#
#     def add_book(self,book):
#         a = input("password: ")
#         if a == "12345":
#             books.append(book)
#             print(f"{book} nomli kitob ro'yxatga qoshildi")
#         else:print("Sizda bunday huquq yoq")
#
#     def remove_book(self,book_name):
#         i = input("password: ")
#         if i == "12345":
#             if book_name in books:
#                 del book_name
#                 return "kitob o'chirildi"
#
#             else:
#                 return "Bu kitob royxatda mavjud emas"
#
#         else:
#             return "Sizda bunday xuquq yo'q"
#
#
#     def list_books(self):
#         return books
#
#
#
# class Ebook(Library):
#     def __init__(self,kitob,muallifi,sahifalari,fayl_hajmi):
#         super().__init__(kitob,muallifi,sahifalari)
#         self.fayl_hajmi = fayl_hajmi
#
#     def download_PDF(self):
#         return f"{self.kitob} yuklab olinmoqda"
#
#
#
#
# ass = Library("aaa","aaaaa",111)
# ass.add_book("www")
# print(ass.list_books())
# ass.remove_book("www")



#2-misol
#
# from abc import ABC , abstractmethod
# class Animal(ABC):
#     def __init__(self,eat,speak):
#         self.eat = eat
#         self.speak = speak
#
#     @abstractmethod
#     def eat(self):
#         pass
#
#     @abstractmethod
#     def speak(self):
#         pass
#
#
# class Bird(Animal):
#     def  __init__(self,animal):
#         self.animal = animal
#
#     def eat(self):
#         return "Don maxsulotlari asosan,qurt-qumursqalar"
#
#     def speak(self):
#         return "......."
#
#
# class Mammals(Animal):
#     def __init__(self,animal):
#         self.animal = animal
#
#     def eat(self):
#         return "O'simlilklar, va maxsus yemishlar"
#
#     def speak(self):
#         if self.speak == "dog":
#             return "woof woof"
#         elif self.speak == "cow":
#             return " mooo"
#         elif self.speak == "sheep":
#             return " maa maa"
#

#3-misol
# class Account:
#     def __init__(self,ism,balans,password):
#         self.ism = ism
#         self.balans = balans
#         self.password = password
#         self.Saving_Account()
#
#     def Saving_Account(self):
#         if self.password == "salom":
#              return "✅Account successfully saved✅"
#         else:print("Invalid password")
#
#
#     def CurrentAccount(self):
#         return """Your current account:
#         balans:........
#         password:.......
#         this year persent your balans: ...."""
#

# aa = Account("ali",1222,'salom')
# print(aa.Saving_Account())

#4-misol
# class Employee:
#     def __init__(self,ism,lavozimi,ish_haqqi):
#         self.ism = ism
#         self.lavozimi = lavozimi
#         self.ish_haqi = ish_haqqi
#
# class Managaer(Employee):
#     def __init__(self,ism,lavozimi,ish_haqqi):
#         super().__init__(ism,lavozimi,ish_haqqi)
#         self.assign_task()
#
#
#     def assign_task(self):
#         pass
#
# class Intern(Employee):
#     def __init__(self,ism,lavozim,ish_haqqi):
#         super().__init__(ism,lavozim,ish_haqqi)
#
#
#     def salary_percent(self):
#         return self.ish_haqi*30/100
#
#
# a = Intern("ali","aaaa",100)
# print(a.salary_percent())


#5-misol
# class Student:
#     def __init__(self,ism,kurs,bahosi):
#         self.ism = ism
#         self.kurs = kurs
#         self.__bahosi = bahosi
#
#     @property
#     def bahosi(self):
#         return self.__bahosi
#     @bahosi.setter
#     def bahosi(self,new):
#         a = input("password: ")
#         if a == "salom":
#             self.__bahosi = new
#             print("baho o'zgartirildi")
#
#     @bahosi.deleter
#     def bahosi(self):
#         s = input("password: ")
#         if s == "baho5":
#             del self.__bahosi
#             return "Baho o'zgartirildi"
# s = Student("ali","2",5)
#
# class GraduateStudent(Student):
#     def __init__(self,ism,kurs,bahosi):
#         super().__init__(ism,kurs,bahosi)
#
#
#
#     def yillik_baholari(self):
#         if self.kurs == 4:
#             return "yillik baholar 5/5/5/5/4/4/3/3/4/5/5"
#
#
#
# class UnderGround(Student):
#     def init(self,ism,kurs,bahosi):
#         super().__init__(ism,kurs,bahosi)
#
#
#     def darsni_tushunishi(self):
#         if self.bahosi == 5:
#             return "Juda yaxshi"
#         elif self.bahosi == 4:
#             return "Qoniqarli"
#         else:return"Yomon"
#
#
#
#
# a = UnderGround("Ali",3,5)





a = 12345
for i in a:
    print(i)
































































