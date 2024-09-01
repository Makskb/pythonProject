from stringprep import map_table_b2

immutable_var = 'laptop', 'windows', 'tabie', 123, '456'
print(type(immutable_var)) # класс данных кортеж (tuple)  является не изменным
# immutable_var [3] = 456
print(immutable_var)
mutable_list = ['laptop', 'windows', 'tabie', 123, '456']
print(type(mutable_list))
mutable_list [3] = 321
mutable_list [4] = int(654)
print(mutable_list)