# Данные о сотрудниках в программе хранятся в словаре
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 47800
    },
]

max = {'name':staff[0]["name"],'surname':staff[0]["surname"],'salary':staff[0]["salary"]}
min = {'name':staff[0]["name"],'surname':staff[0]["surname"],'salary':staff[0]["salary"]}
uniq_surname = {}
summ = 0
names = []

for el in staff:
    if el["salary"] > max["salary"]:
        max = el
    if el["salary"] < min["salary"]:
        min = el
    summ = el["salary"]
    names.append(el["surname"])
    uniq_surname[el["surname"]] = 0
# Вычислите:
print("Имя и Фамилию сотрудника с самой высокой зарплатой:")
print(max)
# TODO: your code here

print("Имя и Фамилию сотрудника с самой низкой зарплатой:")
print(min)

# TODO: your code here
print("Среднеарифметическую зарплату всех сотрудников")
print(summ/len(staff))

# TODO: your code here
number_sun = 0
for surname in uniq_surname:
    if names.count(surname) > 1:
        number_sun += names.count(surname)
    uniq_surname[surname] = names.count(surname)

print("Количество однофамильцев в организации")
print(number_sun)
print(uniq_surname)

# TODO: your code here

print("*Список всех сотрудников(Имя и Фамилию) в порядке возрастания их зарплаты")

# TODO: your code here
