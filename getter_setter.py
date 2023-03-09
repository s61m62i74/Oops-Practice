# from Item import Item
# from phone import phone
# Item.instantiate_from_csv()
# print(Item.all)

from Item import Item

item1 = Item("jondy", "MyItem", 750)
item1.name = "OtherItem"
print(item1.name)
