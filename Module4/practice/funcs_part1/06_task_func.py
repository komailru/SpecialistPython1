# Напишите функцию, которая проверит, что точка (x, y)
# находится строго внутри окружности с центром в точке (xc, yc) и радиусом r:

def distance(p1, p2):
    # TODO: your code here
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**.5

def point_in_circle(x, y, xc, yc, r):
    # TODO: your code here
    return distance((x, y),(xc, yc)) == r

# Не забудьте протестировать вашу функцию

print(point_in_circle(0, 10, 0, 0, 10))
