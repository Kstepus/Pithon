my_dict = {'Stepan': 2001, 'Karalina': 2009, 'Sveta': 2005}
print(my_dict)# здесь я создал словарь
my_dict = {'Stepan': 2001, 'Karalina': 2009, 'Sveta': 2005}
print(my_dict['Stepan'])# здесь я вывел значение этого ключа
del my_dict['Karalina']
print(my_dict)# здесь я удалил ключ со значением
my_dict.update({'Sahsa': 2000,
                'Alex': 1999})
print(my_dict)# здесь я добавил два ключа


my_set =  {1, 'Яблоко', 42.314, 42.314, 1}
print(my_set)
my_set.update({'жолудь', 'банан'})
print(my_set)
del my_set['Яблоко']
print(my_set)