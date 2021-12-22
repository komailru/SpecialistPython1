# Дана строка текста, слова разделены пробелами, знаки препинания отсутствуют.
# Определить в предоставленном сообщении количество слов длиной больше, чем 5.

text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/

# TODO: your code here

count = 0
space_index = text.find(" ")
while space_index >= 0:
    text = text[space_index + 1:]
    word = text[:space_index]
    space_index = text.find(" ")
    if len(word) > 5:
        count += 1
print(count)
