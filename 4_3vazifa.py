from decimal import Decimal
#
# num1 = Decimal(input("son1: "))
# num2 = Decimal(input("son2: "))
# a = Decimal(f"{num1}")+Decimal(f"{num2}")
# print(a)


#--------------------------------------------------------
from decimal import Decimal

#2-misol
# item = input("Maxsulot narxi: ")
# foiz = input("Foiz: ")
#
# print(Decimal(f"{item}")*Decimal(f"{foiz}")/100)

#--------------------------------------------------------
#3-misol

# num = Decimal(input("Son kiriting: "))
# print(num.quantize(Decimal('1.00')))



#--------------------------------------------------------
#4-misol

# a= int(input("birinchi son: "))
# b= int(input('ikkinchi son: '))
# if a > b:
#     print(a)
# elif a< b:
#     print(b)
# else:print("Sonlar teng")
#
#
#


# --------------------------------------------------------
#5-misol
# num = input("Son1: ")
# num2 = input("Son2: ")
# num3 = input("Son3: ")
# print(Decimal(f"{num}")+Decimal(f"{num2}")+Decimal(f"{num3}"))
# print(Decimal(f"{num}")-Decimal(f"{num2}")-Decimal(f"{num3}"))
# print(Decimal(f"{num}")/Decimal(f"{num2}")/Decimal(f"{num3}"))

# --------------------------------------------------------

#6-misol
from decimal import Decimal
#
# ii = Decimal(input("Son: "))
# iii = Decimal(f"{ii}")/Decimal("12.80")
# num = iii.quantize(Decimal('1.00'))
# print(num)
#
# --------------------------------------------------------

#7-misol
# ii = Decimal(input("Son: "))
# print(Decimal(f"{ii}")*2)

# --------------------------------------------------------

#8-misol
# ii = Decimal(input("Kasr son kiriting: "))
# cc = ii.quantize(Decimal('1.'))
# print(Decimal(f'{ii}')%Decimal(f"{cc}"))

# --------------------------------------------------------

#9-misol
# ii = Decimal(input("son kiriting: "))
# print(Decimal(f"{ii}")**3)
# --------------------------------------------------------


#10misol
from decimal import Decimal

# item = input("Number: ")
# foiz = "15"
#
# print(Decimal(f"{item}")*Decimal(f"{foiz}")/100)

# --------------------------------------------------------
#11-misol
# import random
#
# print(random.randint(1,1000))

#12-misol
import random
# ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# other_strings = 'abcdefghijklmnopqrstuvwxyz0123456789'
# simvols = '@#$%&?<>!_'
# all = ascii_uppercase + other_strings + simvols

# while True:
#     length_password = input("Parol uzunligini kiriting: ")
#     if length_password.isdigit():
#         length_password = int(length_password)
#         password = ''
#         for i in range(length_password):
#             iii = random.choice(all)
#             password += iii
#         print("Sizning parolingiz",password)
#     else:print("Iltimos faqat son kiriting!!!")

#13-misol
# import random
#
# tanga = ["oq","gerb"]
# print(random.choice(tanga))
#


#14-misol
# import random
#
#
# random_numbers = random.sample(range(1, 50), 6)
# print(random_numbers)

#15-misol
# import random
#
#
# for i in range(1000):
#     random_numbers = [random.randint(1, 1000)]
#     average_value = sum(random_numbers) / len(random_numbers)
# print("O'rtacha qiymat:", average_value)


#16-misol
import random

#
# r = random.randint(0, 255)  # Qizil kanal (R)
# g = random.randint(0, 255)  # Yashil kanal (G)
# b = random.randint(0, 255)  # Moviy kanal (B)
#
# print(f"Tasodifiy rang (RGB): ({r}, {g}, {b})")



#16-misol

# def choice(list):
#     import random
#     print(random.choice(list))
#
# x = ["s",'e','w','s',2,5,8,54]
# choice(x)


#17-misol

# def arr(list):
#     import random
#     random.shuffle(list)
#     return list
#
# x = ["s",'e','w','s',2,5,8,54]
# print(arr(x))

#18-misol
import math
from math import radians

# a = int(input("son: "))
# print(math.sqrt(a))


#19-misol

# b = int(input("Burchakni kiriting: "))
# print(math.sin(radians(b)))
# print(math.cos(radians(b)))

#20-misol
import math
# asos = float(input("Logarifm asosi (baza) ni kiriting: "))
# qiymat = float(input("Logarifm qiymatini kiriting: "))
# natija = math.log(qiymat, asos)
# print(f"Logarifm ({asos}-asosida {qiymat}) = {natija}")

# #21-misol
# ii = int(input("son: "))
# print(math.factorial(ii))


