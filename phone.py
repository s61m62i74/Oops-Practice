from Item import Item


class phone(Item):

    def __init__(self, name: str, phn: str, price: float, quantity=0, brokenphones=0):  # validate data type
        super().__init__(
            name, phn, price, quantity
        )
        assert brokenphones >= 0, f"brokenphones {brokenphones} is not greater than zero!"

        self.brokenphones = brokenphones
