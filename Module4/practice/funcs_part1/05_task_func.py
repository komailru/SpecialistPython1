# Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), если соединить эти точки отрезками
# и получится треугольник, то нужно найти его периметр и площадь.
# Если по заданным точкам треугольник построить нельзя, выведите соответствующее сообщение.
# Подсказка: для нахождения площади используйте Теорему Герона

# TODO: your code here

# Не забудьте протестировать вашу функцию

def can_triangle(p1, p2, p3):
    # TODO: your code here
    return (p1[0] == p2[0] and p2[0] == p3[0] or p1[1] == p2[1] and p2[1] == p3[1]) != True

def distance(p1, p2):
    # TODO: your code here
    pass
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5

def perimetr(p1, p2, p3):
    return distance(p1, p2) + distance(p2, p3) + distance(p1, p3)

def square(p1, p2, p3):
    p_2 = perimetr(p1, p2, p3) / 2
    return (p_2*(p_2-distance(p1, p2))*(p_2-distance(p2, p3))*(p_2-distance(p1, p3)))**.5

# Пример вызова функции
if can_triangle((10, 12), (14, 18), (12, 12)):
    print("Периметр =",perimetr((10, 12), (14, 18), (12, 12)))
    print("Площадь =",square((10, 12), (14, 18), (12, 12)))
else:
    print("Не треугольник")

# Не забудьте протестировать вашу функцию
