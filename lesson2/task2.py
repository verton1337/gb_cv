"""
Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться,
что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным. 
"""


class ItemDiscount:

    def __init__(self, name, price) :
        self.__name = name
        self.__price = price
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f"{self.get_name()} {self.get_price()}"


print("*"*5, "Parent", "*"*5)
pr = ItemDiscount("Milk", 100)
print(f"{pr.get_name()} {pr.get_price()}")


print("*"*5, "Slave", "*"*5)
rep = ItemDiscountReport("Milk", 100)
print(rep.get_parent_data())