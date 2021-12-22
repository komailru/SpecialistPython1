# Дан кортеж заполненный целыми числами
# Найдите самый большой элемент кортежа
tup = (2, 4, 6, -4, 12, 0, 5)

# TODO: your code here

max_item = tup[0]

for item in tup:
    if item > max_item:
        max_item = item
print(max_item)
