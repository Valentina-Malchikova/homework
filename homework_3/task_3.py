# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(num_1, num_2, num_3):
    summ = num_1 + num_2 + num_3
    return summ - min((num_1, num_2, num_3))
num_1 = int(input('Enter number 1: '))
num_2 = int(input('Enter number 2: '))
num_3 = int(input('Enter number 3: '))
print(my_func(num_1, num_2, num_3))
