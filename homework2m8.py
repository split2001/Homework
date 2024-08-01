def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    try:
        for number in numbers:
            try:
                result += number
            except TypeError:
                incorrect_data = incorrect_data + 1
                print(f'Некорректный тип данных для подсчёта суммы - {number}')
    except TypeError:
            return None
    return result, incorrect_data

def calculate_average(numbers):
    sum = personal_sum(numbers)
    list_ = []
    try:
        for num in numbers:
            if type(num) == int:
                list_.append(num)
        return sum[0]/len(list_)
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
