import string
class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = [file.strip() for file in file_names[0].split(',')]

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:

                    content = file.read().lower()

                    for char in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        content = content.replace(char, ' ')

                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            if word in words:
                result[name] = words.index(word)
            else:
                result[name] = -1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        all_words = self.get_all_words()

        for name, words in all_words.items():
            result[name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())

print(finder2.find('TEXT'))

print(finder2.count('teXT'))

