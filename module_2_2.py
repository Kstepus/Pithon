first = int(input(3))
second = int(input(2))
third = int(input(0))
print('First =', first)
print('Second =', second)
print('Third =', third)
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)
