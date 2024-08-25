import multiprocessing
import time
from datetime import datetime

def read_info(name):
    with open(name, 'r', encoding='utf-8') as f:
        all_data = f.readlines()

time_start = datetime.now()
filenames = [f'./file {number}.txt' for number in range(1, 5)]
for file in filenames:
    read_info(file)
time_end = datetime.now()
time_res = time_end - time_start
print(time_res)


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    time_start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    time_end = datetime.now()
    time_res = time_end - time_start
    print(time_res)



