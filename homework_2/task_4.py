# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.


user = input('Введите строку: ')
user_str = user.split()
num = 1
for user_str in user_str:
    print(f'№{num} - {user_str[:10]}')
    num +=1
