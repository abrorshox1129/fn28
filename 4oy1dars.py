class NameString:
    def __set_name__(self, owner, name):
        self.name = '_'+name


    def __set__(self, instance, value:str):
        if type(value) is str:
            if value.isalpha():
                instance.__dict__[self.name]=value
            else:
                print("Ismni to'g'ri kiriting")
        else:
            print("Ismni to'g'ri kiriting")

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __delete__(self, instance):
        del instance.__dict__[self.name]











class Checkphonenumber:
    def __set_name__(self, owner, name):
        self.item = name
    def __set__(self, instance, value:str):
        if value.startswith("+"):
             if value[1:].isdigit():
                 if len(value) == 13:
                    instance.__dict__[self.item]=value

             else:
                 print("raqam noto'gri kiritildi!!!")

        else:
            print("Raqam notog'ri kiritildi!!!")


    def __get__(self, instance, owner):
        return instance.__dict__[self.item]

    def __delete__(self, instance):
        del instance.__dict__[self.item]




class Person:
    ism = NameString()
    familiya = NameString()
    phonenumber = Checkphonenumber()
    def __init__(self,ism,familiya,phonenumber):
        self.ism =ism
        self.familiya = familiya
        self.phonenumber = phonenumber





# p = Person("ali","aliyev","998911111111")
# print(p.phonenumber)

# p.phonenumber = "998911111221"
# print(p.phonenumber)
#
#
#
#
#
#
# a = "sjdHNII"
# s = []
# for i in a:
#     if i.isupper:
#         s.append(i)
#
#     else:
#         continue
# print(s)
#


import wikipediya



