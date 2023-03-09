# method
class Item:
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = 'shuvam'
item1.phn = 'oneplus'
item1.price = 30000
item1.quantity = 3
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item()
item2.name = 'surjit'
item2.phn = 'vivo'
item2.price = 18000
item2.quantity = 2
print(item2.calculate_total_price(item2.price, item2.quantity))

item3 = Item()
item3.name = 'sambit'
item3.phn = 'motorala'
item3.price = 24624
item3.quantity = 1
print(item3.calculate_total_price(item3.price, item3.quantity))
