# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = int(input("Ведите число: "))
a = []
factorial = 1

for i in range(num):
    factorial = factorial * (i+1)
    a.append(factorial)
print(a)