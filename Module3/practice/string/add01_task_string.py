# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

# TODO: your code here

text = input("Введите строку: ")

i = 0
s = ""
while i < len(text):
    if text[i].isalnum() or text[i] == " ":
        s = s + text[i]
    i += 1
array = s.split(" ")
i = 0
count = 0
while i < len(array):
    if len(array[i]) > 7:
        count += 1
    i += 1
print(count)
