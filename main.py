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