my_dict = {'Darya' : 1996, 'Maxim' : 1984, 'Larisa' : 1971}
print(my_dict)
print(my_dict['Darya'])
print(my_dict.get('Vasiliy'))
my_dict.update({'Vitaliy' : 1973,
                'Vladimir' : 1948,
                'Tanay' : 1948})
print(my_dict)
a = my_dict.pop('Darya')
print(a)
print(my_dict)
my_set = {1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 'Darya', 'Maxim', True}
print(my_set.add(7, ) , my_set.add(8, ))
print(my_set.discard(1))
print(my_set)