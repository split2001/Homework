def fake_divide(first, second):
    division_ = first / second
    try:
        first / second
        return division_
    except ZeroDivisionError:
        print('Error')