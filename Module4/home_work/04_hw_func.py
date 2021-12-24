# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y
# ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.

# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# TODO: your code here


#evaluate_str = "-1 5/6 + 1 4/7"
def short(d):
    sep_div   = d.find("/")
    sep_blank = d.find(" ")

    if sep_blank < 0:
        if sep_div < 0:
            return (int(d),1)
        else:
            cc = 0
            dc = d
    else:
        cc = int(d[:sep_blank])
        dc = d[sep_blank+1:]

    sep_div = dc.find("/")
    d_down = int(dc[sep_div+1:])
    if cc < 0:
        d_up   = -(-cc * d_down + int(dc[:sep_div]))
    else:
        d_up = cc * d_down + int(dc[:sep_div])
    return d_up, d_down

def dsumm(d1, d2):
    return d1[0] * d2[1] + d1[1] * d2[0], d1[1] * d2[1]

def evaluate(d1, d2, d):
    d1 = short(d1)
    d2 = short(d2)
    print(d1, d2)
    if d == "+":
        return dsumm(d1, d2)
    else:
        return dsumm(d1, (-d2[0], d2[1]))

# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

evaluate_str = "-2/3 - -2"
print(evaluate_str)

separator_plus = " + "
separator_minus= " - "

sep = evaluate_str.find(" + ")
d = "+"
if sep < 0:
    sep = evaluate_str.find(" - ")
    d = "-"
if sep > 0:
    result = evaluate(evaluate_str[:sep], evaluate_str[sep+3:], d)
    print(result)
    if result[0] > 0:
        сс = result[0] // result[1]
        result = str(сс) + " " + str(result[0] - сс * result[1]) + "/" + str(result[1])
    else:
        сс = -result[0] // result[1]
        result = "-" + str(сс) + " " + str(-result[0] - сс * result[1]) + "/" + str(result[1])
else:
    result = "ошибка ввода"


#result = print(evaluate_str[:sep],evaluate_str[sep+3:],d,sep="|")
print(result)
