# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here

if len(names) > 0:
	longest_name = names[0]		
else:
	longest_name = ""

for name in names:
	if len(name) > len(longest_name):
		longest_name = name

print(longest_name)	
