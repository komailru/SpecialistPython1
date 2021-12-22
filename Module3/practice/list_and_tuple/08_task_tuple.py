# Даны примеры создания кортежей.
# Выясните, какие из них являются корректными.
# Все некорректные объявления и создающие не котрежи закомментируйте (#)
tup1 = (2, 4, -6)
print("1",type(tup1),tup1)
tup2 = (2, "Василия", -6)
print("2",type(tup2),tup2)
tup3 = 2, 4, -6
print("3",type(tup3),tup3)
tup4 = (2)
print("4",type(tup4),tup4)
tup5 = (2,)
print("5",type(tup5),tup5)
tup6 = 2,
print("6",type(tup6),tup6)
tup7 = tuple([2, 4, -6, 12])
print("7",type(tup7),tup7)
#tup8 = tuple(2, 7, 8, -5)
#print("8",type(tup8),tup8)
tup9 = tuple()
print("9",type(tup9),tup9)
tup10 = tuple("hello")
print("10",type(tup10),tup10)
tup11 = ()
print("11",type(tup11),tup11)
tup12 = 2 and 4
print("12",type(tup12),tup12)
