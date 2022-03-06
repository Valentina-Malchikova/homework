# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

with open('text_2.txt') as file:
    file_lines = file.readlines()

employees = {}
sum_salary = 0
for line in file_lines:
    employeers_info = line.split()
    employees.update({employeers_info[0]: float(employeers_info[1])})
    sum_salary += float(employeers_info[1])
average_salary = sum_salary / len(employees)
print(f'Average = {average_salary}')

for k, v in employees.items():
    if v < 20000:
        print(f'{k}: {v}')
