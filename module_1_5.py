immutable_var = ('Boris', 12, False, 12.48, [132, 231])
print(immutable_var)
immutable_var [4][0]=[65] # - в кортеже можно поменять только изменяемые объекты
print(immutable_var)
# - в кортеже нельзя производить замены как это можно делать в списке, кроме добавление припомощи знаков + и *
mutable_list = [5, 16, 25]
print(mutable_list)
mutable_list[0] = 35
print(mutable_list)