# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех положительных элементов.

# TODO: your code here

n = [10, -10, 5]

summ_items = 0
for item in n:
    if item > 0:
        summ_items += item
print(summ_items)
