# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here

text = input("Введите строку ")

array_of_string = text.split(" ")

i = 0
quantity = 0

while i < len(array_of_string):
    if len(array_of_string[i]) >= 5:
        quantity = quantity + 1
    i += 1
print(quantity)
