# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

num_month = input('Введите номер месяца: ')
wint, spr, summ, aut = 'winter', 'spring', 'summer', 'autumn'
year_dict = {'1':wint, '2':wint, '3':spr, '4':spr, '5':spr, '6':summ, '7':summ, '8':summ, '9':aut, '10':aut, '11':aut, '12':wint}
print(year_dict[num_month])
list_season = [wint, wint,spr, spr, spr, summ, summ, summ, aut, aut, aut, wint]
print(list_season[int(num_month) - 1])
