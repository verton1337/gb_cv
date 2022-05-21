"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345). Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого. 

"""
import os

def simpleFile():
    if os.path.exists(os.path.abspath("simpleFile.txt")):
        print("File is exists")
        exit()
    else:
        with open("words.txt", "r") as fw:
            words = fw.read().split(" ")
        numbers = [n for n in range(555, 666)]
        result = zip(words, numbers)
        with open("simpleFile.txt", "w") as f:
                for w, n in result:
                    f.write(f"{w}{n}\n")

    return os.path.abspath("simpleFile.txt")



def readSimpleFile(fileName):
    with open(fileName, "r") as f:
        for word in f.readlines():
            print(word)




if __name__ == "__main__":
    path = simpleFile()
    readSimpleFile(path)

