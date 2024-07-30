def add_everything_up(a, b):
    try:
        print(round(a+b))
    except TypeError as error:
        print(f'Получаем результат - "{str(a)} +{str(b)}" несмотря на ошибку:{error}')

add_everything_up(123.456, 'строка')
add_everything_up('яблоко', 4215)
add_everything_up(123.456, 7)