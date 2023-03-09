import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                phn=item.get('phn'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f" Item ('{self.name}', {self.phn} , {self.price} , {self.quantity})"


print(Item.is_integer(7.0))
