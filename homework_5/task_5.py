# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import  random

with open('text_5.txt', 'w') as file:
    for _ in range(25):
        file.write(f'{random.randint(0, 15)} ')
with open('text_5.txt') as file:
    num_str = file.read().split()
    sum = 0
    for num in num_str:
        sum += int(num)
print(sum)
