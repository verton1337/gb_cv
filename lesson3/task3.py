"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None. Если есть  значения, которым не хватило ключей, их необходимо отбросить. 
"""

def get_dict(keysList, valuesList):
    #Копирую список, чтобы при изменении списка внутри функции не поменять исходный список
    vl = valuesList.copy()
    if len(keysList) > len(vl):
        for i in range(len(vl), len(keysList)):
            vl.append(None)
    return dict(zip(keysList, vl))




if __name__ == "__main__":

    keysList = ["1", "2", "3"]
    valuesList = [3, 2, 1]
    print(get_dict(keysList, valuesList))

    keysList = ["1", "2", "3", "4"]
    valuesList = [3, 2, 1]
    print(get_dict(keysList, valuesList))


    keysList = ["1", "2"]
    valuesList = [3, 2, 1]
    print(get_dict(keysList, valuesList))


    

