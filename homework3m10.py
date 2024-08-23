import random
from random import randint
import time
from threading import Thread, Lock
import threading


class Bank:
    def __init__(self, balance=0):
        self.lock = threading.Lock()
        self.balance = balance

    def deposit(self):
        for i in range(100):
            random_ = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance = self.balance + random_
                print(f'Пополнение: {random_}. Баланс: {self.balance}.')
                time.sleep(0.001)

    def take(self):
        for i in range(100):
            random_ = random.randint(50, 500)
            print(f'Запрос на {random_}')
            if self.balance >= random_:
                self.balance = self.balance - random_
                print(f'Снятие: {random_}. Баланс: {self.balance}')
                time.sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                time.sleep(0.001)
                self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
