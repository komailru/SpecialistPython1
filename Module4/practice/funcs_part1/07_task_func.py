# Напишите функцию принимающую время в секундах и возвращающую строку формата: “hh:mm:ss”,
# где hh - часы, mm- минуты, ss - секунды.
# Пример:
# 29143 секунд → 08:05:43

def my_time(second):
    hours = second // 3600
    minutes = (second - hours * 3600) // 60
    seconds = second - hours * 3600 - minutes * 60
    return f"{hours:0>2}:{minutes:0>2}:{seconds:0>2}"

print(my_time(29143))
