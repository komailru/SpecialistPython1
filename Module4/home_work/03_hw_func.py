# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here

def distance(x1, y1, x2, y2):
    # TODO: тело, которое вы реализовали на практической работе
    return ((x1 - x2)**2 + (y1 - y2)**2)** .5


p1 = (0, 0)
R1 = 10
p2 = (0, 5)
R2 = 5.1

diff_center = distance(*p1, *p2)

print(diff_center + R1 <= R2 or diff_center + R2 <= R1)
