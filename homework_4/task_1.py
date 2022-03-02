# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

import sys
if len(sys.argv) < 4:
    print(f'Введите данные: выработка в часах, ставка в час, премия')
else:
    production = float(sys.argv[1])
    rate = float(sys.argv[2])
    premium = float(sys.argv[3])
    result = production * rate + premium
    print(result)

