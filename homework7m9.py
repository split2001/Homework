def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result == 1:
            print('Не является ни простым, ни составным')
        elif result == 2:
            print('Простое число')
        elif result % 2 == 0:
            print('Составное число')
        else:
            print('Простое число')
    return wrapper

# @is_prime
# def sum_three(*args):
#     result_ = 0
#     for i in args:
#         result_ += i
#     return result_

@is_prime
def sum_three(a, b, c):
    result_ = a + b + c
    print(result_)
    return result_


sum_three(2, 3, 6)

