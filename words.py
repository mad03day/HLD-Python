#!/usr/bin/python3

import sys  #import system package for work with command lines arguments

"""
Скрит, що відкриває файл та фіксує кількість повторів кожного слова.
Виводить на екран слово та кількість його повторів. Другим аргументом скрипта є обмеження, тобто виводитимуться на екран усі слова, що повторюються більше за n кількість

"""

def word_collection(name, n):
    text = open(name, 'r').read()   #Open file as read and read him
    text = text.lower()             
    words = set(text.split())       
    for word in words:
        if text.count(word) >= n:
            print("Word: {}, count: {}".format(word, text.count(word)))

"""
Перевіряємо як саме запускається файл, якщо у якості __main__ то запускаємо наш скрипт, в інших випадках даний файл використовується як бібліотека, а отже не повинен працювати як скрипт
"""

if __name__ == "__main__":
    file_name = str(sys.argv[1])
    n_limit = int(sys.argv[2])
    word_collection(file_name, n_limit)
