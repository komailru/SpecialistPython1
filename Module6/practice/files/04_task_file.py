# Дан файл ("data/fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А.txt, fruits_Б.txt, fruits_В.txt ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв,
#        а также есть пустые строки, которые нужно пропустить.
# Напишите универсальный код, который будет работать с любым списком фруктов и
# распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.

# Возможно пригодится:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

my_path = "data_files/"
name_in = "fruits.txt"

output = {}

f = open(my_path+name_in, "r", encoding="utf-8")
for line in f:
    if len(line) == 1:
        continue
    First_letter = line[:1]
    if output.get(First_letter) == None:
        output[First_letter] = []
    output[First_letter].append(line)
f.close()
print(output)

for el in output:
    f = open(my_path+"fruits_"+el, "w", encoding="utf-8")
    for item in output[el]:
        f.write(item)
    f.close()
