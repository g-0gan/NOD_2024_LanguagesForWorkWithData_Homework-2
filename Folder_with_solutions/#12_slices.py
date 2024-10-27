# Глобальная константа
WORD = 'объектно-ориентированный'

# Составляем слова с помощью индексации и срезов
word1 = WORD[:6]            # объект
word2 = WORD[9:17]          # ориентир
word3 = WORD[14:17]         # тир
word4 = WORD[4] + WORD[0] + WORD[5]  # кот
word5 = WORD[10] + WORD[12:15] + WORD[19]  # рента

# Выводим результаты
print(word1)  # объект
print(word2)  # ориентир
print(word3)  # тир
print(word4)  # кот
print(word5)  # рента


