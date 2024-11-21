import sys
from time import sleep


class User:

    def __init__(self, nickname, password,age):
        self.nickname = str(nickname)
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    time_now = 0

    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode


class UrTube:

    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):
        user_exist = False
        for i in self.users:
            if i.nickname == nickname and i.password == hash(password):
                self.current_user = i
                user_exist = True
        if not user_exist:
            print('Ошибка входа')

    def register(self, nickname, password, age):
        user_exist = False
        for i in self.users:
            if i.nickname == nickname:
                user_exist = True
                print(f'Пользователь {nickname} уже существует')
                break
        if not user_exist:
            user = User(nickname,password,age)
            self.users.append(user)
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i in self.videos:
                continue
            else:
                self.videos.append(i)

    def get_videos(self, videoname):
        found_videos = []
        for i in self.videos:
            if videoname.lower() in i.title.lower():
                found_videos.append(i.title)
        return  found_videos

    def watch_video(self, videoname):
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for i in self.videos:
            if videoname.lower().strip() == i.title.lower():
                if i.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                for j in range(1,i.duration+1):
                    print(j, end=' ')
                    sleep(1)
                print('Конец видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')