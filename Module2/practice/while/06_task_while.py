# Два натуральных числа называются дружественными, если каждое из них равно сумме всех натуральных делителей другого
# (само число при этом не рассматривается в качестве собственного делителя).
# Необходимо найти все пары натуральных дружественных чисел (не равных друг другу),
# оба числа в которых меньше вводимого с клавиатуры числа N.
# Дано натуральное число n, требуется проверить его на простоту.

# Формат входных данных: Вводится одно целое число N (1≤N≤10000).
# Формат выходных данных: Требуется вывести все пары дружественных чисел,
# удовлетворяющие условию задачи. Пары можно выводить в любом порядке.

# Пример:
# Входные данные
# 300
# Выходные данные
#
# 220 284
# 284 220

# TODO: your code here

N = int(input("Введите целое число "))

first_number = 2

while first_number <= N:
    i = 1
    sum1 = 0
    while i < first_number:
        if first_number % i == 0:
            sum1 += i
        i += 1
    if 1 < sum1 <= N:
        #print(sum1)
        i = 1
        second_number = sum1
        sum2 = 0
        while i < sum1:
            if sum1 % i == 0:
                sum2 += i
            i += 1
        if first_number == sum2 and first_number != second_number:
            print(first_number," ",second_number)
    first_number += 1
