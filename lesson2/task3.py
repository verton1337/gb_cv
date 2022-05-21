"""
Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию о товаре.

"""


class ItemDiscount:

    def __init__(self, name, price) :
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    def set_name(self, newName):
        self.__name = newName

    def set_price(self, newPrice):
        self.__price = newPrice


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f"{self.get_name()} {self.get_price()}"



rep = ItemDiscountReport("Milk", 100)

print("*"*5, "Old name and price", "*"*5)
print(rep.get_parent_data())

rep.set_name("Bread")
rep.set_price(20)

print("*"*5, "New name and price", "*"*5)
print(rep.get_parent_data())