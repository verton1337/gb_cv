"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы (вторая и третья строка после объявления дочернего класса). 
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
    def __init__(self, name, price, salePercent):
        self.__salePercent = salePercent
        super().__init__(name, price)
    

    def get_parent_data(self):
        return f"{self.get_name()} {self.get_price()}"

    def __str__(self) -> str:
        return f"{self.get_price()*(100 - self.__salePercent)/100}"



rep = ItemDiscountReport("Milk", 100, 20)

print("*"*5, "Standart price", "*"*5)
print(rep.get_parent_data(), end = "")
print(f" and sale price is {rep}")

