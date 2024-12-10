# import json
#
#
# data = {
#     'id':1223,
#     'full_name':'Toxir Toxirov',
#     'phone':['998912344','99877363'],
#     'man':True
# }

# file = open("user.json",mode='w',encoding='utf-8')
# json.dump(data,file)
# file.close()

# file = open("user.json",mode='r',encoding='utf-8')
# data = json.load(file)
# print(type(data))
# print(data)

import json
file = open("foods.json", mode="r", encoding="utf-8")
iii = json.load(file)
print(iii)


































