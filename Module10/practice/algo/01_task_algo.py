# "Карточки"
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

N = int(input("Введите максимальный номер карточки "))

i = 1
sum_cards_numbers = 0
sum_all = N
while i <= N-1:
    new_number = int(input("Введите номер карточки "))
    sum_cards_numbers = sum_cards_numbers + new_number
    sum_all += i
    i += 1
print("Потеряли",sum_all - sum_cards_numbers)
