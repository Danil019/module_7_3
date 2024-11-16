class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}  # Словарь для хранения слов по файлам
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower().replace('!', '').split()  # Приводим к нижнему регистру и разбиваем на слова
                all_words[file_name] = words  # Записываем в словарь, ключ — имя файла
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        for file_name, words_list in self.get_all_words().items():
            position = words_list.index(word) + 1
            results[file_name] = position
            return results

    def count_word(self, word):
        word = word.lower()
        results = {}
        for file_name, words_list in self.get_all_words().items():
            count = words_list.count(word)
            results[file_name] = count
            return results


wrd1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(wrd1.get_all_words())
print(wrd1.find('captain'))
print(wrd1.count_word('captain'))
