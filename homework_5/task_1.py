# Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open('text.txt', 'w') as file:
    input_text = input('Your text: \n')
    while input_text:
        file.write(f'{input_text}\n')
        input_text = input('Your text:\n')
