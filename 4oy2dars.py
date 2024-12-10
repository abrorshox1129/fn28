# text ="Hello World"
# print(id(text))
# print(hex(id(text)))
# print(oct(id(text)))
# print(bin(id(text)))



import time

current_time = time.time()

now = time.strftime(f"%H:%M:%S")
print(now)

#
# start = time.time()
# for i in range(100):
#     time.sleep(0.2)
#     print(i)
#
# # end = time.time()
# # print(end - start)


from datetime import date

current_date = date.today()
print(current_date)
print(current_date.day)
print(current_date.month)
print(current_date.year)













