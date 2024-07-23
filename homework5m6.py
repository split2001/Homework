import io
from pprint import pprint

def custom_write(file_name, strings):
    dict_ = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for string in strings:
            position = file.tell()
            file.write(string)
            dict_[len(dict_) + 1, (position)] = string
    return dict_

info = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)