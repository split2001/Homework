first = input('Введите целое число №1:')
second = input('Введите целое число №2:')
third = input('Введите целое число №3:')
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif not first == second and not second == third:
    print(0)
