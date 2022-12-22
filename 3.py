# 3 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input("Ведите число: "))
a = []
num > 0
result = 1.0
for i in range(num):
    result = (1+1/(i+1))**(i+1)
    a.append(result)
print(a)
result = sum (a)
print(result)