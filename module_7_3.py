from idlelib.iomenu import encoding
import re

class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        word = {}
        for el in self.file_names:
            with open(el, 'r', encoding='utf-8') as file:
                s = file.read().lower()
                f = re.sub(r'[,.=!?;:-]', '', s)
                word[el] = f.split()
        return word

    def __word_in_value(self, func, word):
        slovar = {}
        for key, value in self.get_all_words().items():
            if word.lower() in value:
                if func == 'find':
                    slovar[key] = value.index(word.lower()) +1
                elif func == 'count':
                    slovar[key] = value.count(word.lower())
            return slovar

    def find(self, word):
        return self.__word_in_value('find', word)

    def count(self, word):
        return self.__word_in_value('count', word)


finder2 = WordsFinder('2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('кошка')) # 3 слово по счёту
print(finder2.count('кошка')) # 4 слова teXT в тексте всего


