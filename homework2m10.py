from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name: str, power: int, warriors = 100):
        super().__init__()
        self.name = name
        self.power = power
        self.warriors = warriors

    def run(self):
        day = 0
        print(f"{self.name}, на нас напали!")
        while self.warriors > 0:
            self.warriors -= self.power
            time.sleep(1)
            day += 1
            print(f"{self.name} сражается {day} дней(дня), осталось {self.warriors} воинов.")
        else:
            print(f"{self.name} одержал победу спустя {day} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
