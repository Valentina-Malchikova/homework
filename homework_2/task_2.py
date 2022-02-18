# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


my_list = input('Введите данные: ')
list_input = my_list.split()
len_my_list = len(list_input)
i = 0
while i < len_my_list - 1:
    list_input[i], list_input[i+1] = list_input[i+1], list_input[i]
    i += 2
print(list_input)
