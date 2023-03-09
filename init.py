class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, phn: str, price: float, quantity=0):  # validate data type
        assert price >= 0, f"price {price} is not greater than zero!"

        assert quantity >= 0, f"quantity {quantity} is not greater than zero!"
        self.name = name
        self.phn = phn
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate

    def __repr__(self):
        return f" Item ('{self.name}', {self.phn} , {self.price} , {self.quantity})"


item1 = Item('Shubham', 'oneplus', 30000, 3)
item2 = Item('surjit', 'vivos', 18000, 2)
item3 = Item('Gambit', 'motorola', 24624, 5)

print(Item.all)
