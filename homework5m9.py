class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError('Шаг указан неверно')
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = 0


    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        current = self.pointer
        if current > self.stop and self.step > 0 or current < self.stop and self.step < 0:
            raise StopIteration
        else:
            self.pointer += self.step
            return current


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
