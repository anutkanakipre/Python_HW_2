# Реализуйте алгоритм перемешивания списка.

list_1 = ["1", "2", "3", "4", "5"]

import random

def mix_list(list_1):
        list = list_1[:] # Цикл от 0 до длины списка -1
        list_length = len(list)
        for i in range(list_length):
            index_mix = random.randint(0, list_length - 1) # Замена
            temp = list[i]
            list[i] = list[index_mix]
            list[index_mix] = temp # Возвращаем список
    
            return list

list = ["1", "2", "3", "4", "5"]
mixed_list = mix_list(list)
print("Первоначальный список: ")
print(list_1)
print("Перемешаный список: ")
print(mixed_list)