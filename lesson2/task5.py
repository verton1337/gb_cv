"""
Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
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


class FirstSlaveItem(ItemDiscount):
    def get_info(self):
        return f"Name is {self.get_name()}"


class SecondSlaveItem(ItemDiscount):
    def get_info(self):
        return f"Price is {self.get_price()}"



def testTask(item):
    print(item.get_info())


cl1 = FirstSlaveItem("Milk", 100)
cl2 = SecondSlaveItem("Bread", 20)

testTask(cl1)
testTask(cl2)
