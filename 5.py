# Строки в Питоне сравниваются на основании значений символов. 
# Т.е. если мы захотим выяснить, что больше: «Apple» или «Яблоко», – то «Яблоко» окажется бОльшим. 
# А все потому, что английская буква «A» имеет значение 65 (берется из таблицы кодировки), 
# а русская буква «Я» – 1071 (с помощью функции ord() это можно выяснить). 
# Такое положение дел не устроило Анну. Она считает, что строки нужно сравнивать по количеству входящих в них символов. 
# Для этого девушка создала класс RealString и реализовала озвученный инструментарий. 
# Сравнивать между собой можно как объекты класса, так и обычные строки с экземплярами класса RealString. 
# К слову, Анне понадобилось только 3 метода внутри класса (включая __init__()) для воплощения задуманного.

class RealString:
    def __init__(self, word1, word2):
        self.__word1 = word1
        self.__word2 = word2

    def bigest_word_self(self):
        w1 = len(self.__word1)
        w2 = len(self.__word2)
        if w1 > w2:
            print("First word is bigger")
        elif w1 < w2:
            print("Second word is bigger")
        else:
            print("Both words are equel")
    
    @staticmethod
    def bigest_word(word1, word2):
        if word1 > word2:
            return print("First word is bigger")
        elif word1 < word2:
            return print("Second word is bigger")
        else:
            return print("Both words are equel")

word1 = str(input())
word2 = str(input())
real = RealString(word1, word2)
real.bigest_word_self()
RealString.bigest_word(word1, word2)