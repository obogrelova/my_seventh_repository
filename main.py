class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.item = {}

    def add_item(self, item_name, price):
        self.item[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.item[item_name]
            print(f"Товар '{item_name}' удален.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена на {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден.")

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"



    store1 = Store("Fruit Paradise", "123 Main St")
    store2 = Store("Tech Haven", "456 Tech Blvd")
    store3 = Store("Book World", "789 Book Ave")

    store1.add_item("apples", 0.5)
    store1.add_item("bananas", 0.75)

    store2.add_item("laptop", 1000)
    store2.add_item("smartphone", 600)

    store3.add_item("novel", 15)
    store3.add_item("textbook", 40)



    print(store1)

    store1.add_item("oranges", 0.65)

    store1.update_price("bananas", 0.80)

    price = store1.get_price("apples")
    print(f"Цена на 'apples': {price}.")

    price = store1.get_price("pears")
    print(f"Цена на 'pears': {price}.")

    store1.remove_item("oranges")

    store1.remove_item("pears")

    print(store1)