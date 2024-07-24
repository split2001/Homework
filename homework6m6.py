from pprint import pprint
import string

class WordsFinder:
    def __init__(self,*file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name,'r', encoding= 'utf-8') as f:
                string = f.read().lower()
                string_punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for p in string_punctuation:
                    if p in string:
                        string = string.replace(p, '')
                all_words[self.file_names] = string.split()
        return all_words

    def find(self, word):
        dict_1 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                index_ = words.index(word.lower())
                dict_1[self.file_names] = index_ + 1
                return dict_1

    def count(self, word):
        dict_2 = {}
        for name, words in self.get_all_words().items():
            amount = words.count(word.lower())
            dict_2[self.file_names] = amount
            return dict_2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

