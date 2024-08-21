import time
from threading import Thread
from datetime import datetime



time_start = datetime.now()
def wite_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f'Какое-то слово № {word + 1}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')

time_start = datetime.now()

the_first = Thread(target = wite_words, args= (10,'example5.txt'))
the_second = Thread(target = wite_words,args=(30,'example6.txt'))
the_third = Thread(target = wite_words,args=(200,'example7.txt'))
the_fourth = Thread(target = wite_words, args=(100,'example8.txt'))

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'Работа потоков {time_res}')
