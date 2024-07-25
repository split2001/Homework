import os
import time
for root, dirs, files in os.walk('.'):
  for file in files:
    filepath = os.path.join('homeworkm7.py')
    filetime = os.path.getmtime('homeworkm7.py')
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize('homeworkm7.py')
    parent_dir = os.path.dirname('homeworkm7.py')
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,Время изменения: {formatted_time} ,'
          f' Родительская директория: {parent_dir}')