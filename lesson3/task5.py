""""
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно) 
заменить на значения типа 345example (в обратном порядке, число и строка). 
Реализовать функцию поиска определенных подстрок в файле по следующим условиям: 
вывод первого вхождения, вывод всех вхождений. Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
"""

from fileinput import filename
import os
import random
from unittest import result

def simpleFile():
    if os.path.exists(os.path.abspath("simpleFile.txt")):
        print("File is exists")
        exit()
    else:
        with open("words.txt", "r") as fw:
            words = fw.read().split(" ")
        numbers = [n for n in range(55, 66)]
        result = zip(words, numbers)
        with open("simpleFile.txt", "w") as f:
                for w, n in result:
                    if random.randint(1, 10) > 4:
                        f.write(f"{w}{n}\n")
                    else:
                        f.write(f"{n}{w}\n")

    return os.path.abspath("simpleFile.txt")



def readSimpleFile(fileName):
    with open(fileName, "r") as f:
        for word in f.readlines():
            print(word)

def searchStr(fileName, substr, cond = "first"):
    with open(fileName, "r") as f:
        if cond == "first":
            for line in f.readlines():
                if substr in line:
                    return line

        if cond == "all":
            result = []
            for line in f.readlines():
                if substr in line:
                    result.append(line) 
            return result

def editAllSubs(fileName, substr, newval):
    with open(fileName, "r") as f:
        oldFile = f.readlines()
    for i in range(len(oldFile)):
            if substr in oldFile[i]:
                oldFile[i] = oldFile[i].replace(substr, newval)
    with open(fileName, "w") as f:
        f.writelines(oldFile)
    for line in oldFile:
        print(line)


if __name__ == "__main__":
    path = simpleFile()

    print("*"*10, "File body", "*"*10)
    readSimpleFile(path)

    print("*"*10, "First Substring", "*"*10)
    print(searchStr(path, "rem", "first"))

    print("*"*10, "All Substrings", "*"*10)
    allSubs = searchStr(path, "rem", "all")
    print(allSubs)

    print("*"*10, "replace All Substrings", "*"*10)
    editAllSubs(path, "rem", "number")