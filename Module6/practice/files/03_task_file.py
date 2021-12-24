# В файлк salaries.txt даны зарплаты сотрудников

# Задача: выведите всех сотрудников в файл highly_paid.txt, зарплаты которых превышают 60000
# Сотрудников вывести в формате: Фамилия И.О. ,например: Иванов И.П. (зарплаты в файл не записывать)

path_in = "data_files/salaries.txt"
path_out = "data_files/highly_paid.txt"
f = open(path_in, "r", encoding="utf-8")
f_out = open(path_out, "w", encoding="utf-8")

hi_paid = []
my_keys = ["фамилия", "имя", "отчество", "зарплата"]

for line in f:
    current_values = []
    for el in line.split():
        if el == "Фамилия":
            break
        else:
            current_values.append(el)
    if el != "Фамилия":
        new_item = dict(zip(my_keys, current_values))
        hi_paid.append(new_item)

f.close()

for el in hi_paid:
    if float(el["зарплата"]) > 60000:
        new_string = el["фамилия"]+" "+el["имя"][:1]+"."+el["отчество"][:1]+"."
        print(new_string)
        f_out.write(new_string+"\n")
f_out.close()
