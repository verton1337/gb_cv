"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.

"""


def checkNumber(number):
    numList = str(number).split(".")
    if len(numList) == 1:
        return "Целое"
    else:
        return ("Дробное", int(numList[0]) == int(numList[1]))




if __name__ == "__main__":
    userInput = input("Enter a number: \n")

    try:
        float(userInput)
    except ValueError:
        print("Not a number!")
        exit()

    print(checkNumber(userInput))
