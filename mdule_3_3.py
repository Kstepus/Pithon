# задание №1
def print_params(a = 1, b = 'ctring', c = True):
   print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
print_params(a='один', b='два', c='три')
# задание №2
def print_params(a, b, c):
    print(a, b, c)
    
values_list_ = [bool, 3, 'привет']
values_dict_ = {'a':1, 'b':2, 'c': 3}

print_params(*values_list_)
print_params(**values_dict_) 
# задача №3
def print_params(a = 111, b = 456, c = 371):
    print(a, b, c)
    
values_list_2 = [54.32, 'Строка']

print_params(*values_list_2, 42)

