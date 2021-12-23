# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]

# TODO: your code here

brands_list = []
brands_price_details = {}
brands_quantity_details = {}

for el in items:
	brand = el["brand"]
	if brands_list.count(brand) == 0:
		brands_list.append(brand)
		brands_price_details[brand] = el["price"]
		brands_quantity_details[brand] =  0
	if brands_price_details[brand] < el["price"]:
		brands_price_details[brand] = el["price"]
	brands_quantity_details[brand] +=  1	
print("Товары на складе представлены брэндами: ")
print(brands_list)	

print("На складе самый дорогой товар брэнда(ов): ")
print(brands_price_details)

print("На складе больше всего товаров брэнда(ов): ")
print(brands_quantity_details)
