# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def info(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'
n = input('Enter your name: ')
s = input('Enter your surname: ')
y = input('Enter year of birth: ')
c = input('Enter city: ')
e = input('Enter your email: ')
p = input('Enter your phone number: ')
result = info(name=n, surname=s, year=y, city=c, email=e, phone=p)
print(result)
