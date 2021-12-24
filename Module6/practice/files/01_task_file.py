# Дан файл data/limericks.txt с лимериками(короткими стихотворениями)

# 1. Выведите содержимое файла в консоль
# 2. Узнайте количество непробельный символов в данном файле.
# Пробельные символы: " " - пробел, "\n" - перенос строки, "\t" - табуляция
# 3. Узнайте количество стихотворений, если известно,
# что каждое стихотворение отделяется ровно одной пустой строкой от предыдущего и после последнего нет пустой строки

path = "data_files/limerics.txt"  # вместо dir подставь название папки с файлом.
# Или удалите dir, если limericks.txt в тойже папке что и текущий файл

# Открываем файл на чтение
f = open(path, "r", encoding="utf-8")
number_symblos = 0
number_poems   = 0
# В переменную line считываем строку за стройкой из файла(f)
for line in f:
    print(line.rstrip())
    number_symblos = number_symblos + len(line.strip())
    if len(line) == 1:
        number_poems += 1
if number_symblos > 0:
    number_poems += 1
print(number_symblos)
print(number_poems)

# Подсказка: пустые строки выглядят так "\n". Помните? Строка считывается вместе с символом переноса!
# Применение метода "\n".rstrip() --> "" вернет вам пустую строку, строку из НУЛЯ символов.
