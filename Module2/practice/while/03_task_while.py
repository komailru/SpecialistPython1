# По данному натуральному n выведите лесенку из n ступенек, i-я ступень состоит из чисел от 1 до i без пробелов.
# Формат входных данных: Вводится натуральное число n.
# Формат выходных данных: Выведите ответ на задачу.
# Пример:
# Для n = 4
# Нужно вывести:
# 1
# 12
# 123
# 1234

# TODO: your code here

n = int(input("Введите натуральное число "))

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j,end="")
        j += 1
    print()
    i += 1
