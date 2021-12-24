# Даны номер месяца и номер года. Найдите сколько дней в этом месяце.
# При вводе неверного номера месяца или некорректного значения программа должна сообщить об ошибке
# и попросить ввести корректные данные. Также необходимо учесть високосный или не високосный год.
# Алгоритм проверки на високосный год оформите в виде отдельной функции.
#
# Входная строка содержит два целых числа – номер месяца (возможно, неправильный) и номер года.

while True:
    try:
        year = int(input("Введите год: "))
        month = int(input("Введите номер месяца: "))
        if 0 < month < 13:
           break
        else:
            print("Месяц должен быть от 0 до 12!")
    except:
        print("Вы ввели не целое число!")

monthes = {1:31,2:28,3:31}

if month == 2 and year % 4 == 0 and year % 100 != 0:
    print(29)
else:
    print(monthes[month])
