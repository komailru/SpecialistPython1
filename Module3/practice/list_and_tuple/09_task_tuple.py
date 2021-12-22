# Дано 3 кортежа заполненные произвольными целыми числами.
# Найдите количество элементов, которые встречаются во всех трех кортежах.

# TODO: your code here

k1 = 10,12,13
k2 = 10,13
k3 = 13,

k = k1,k2,k3

count_ = 0
i = 0
ind = 0
length = len(k[0])
for item in k:
    if len(item) > length:
        length = len(item)
        ind = i
    i += 1
for item in k[ind]:
    j = 0
    found = 0
    while j < 3:
        if j != ind and k[j].count(item) > 0:
            found += 1
        j += 1
    if found == 2:
        count_ += 1
print(count_)
