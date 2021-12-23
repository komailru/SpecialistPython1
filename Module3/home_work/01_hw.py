# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр

text = ""
for name in names:
	text = text + name + ", "
length = len(text)
if length > 0:	
	text = text[:length-2]
print(text)
