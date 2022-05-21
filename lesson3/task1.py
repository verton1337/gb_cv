"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться путь и имя файла с расширением.
В функции необходимо реализовать поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения).
Расширений может быть несколько (например testfile.tar.gz).

"""
import sys
import os
def get_name(path):
    if os.name == 'nt':
        return path.split("\\")[-1].split(".")[0]
    return path.split("/")[-1].split(".")[0]



if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        print("No path found")
        exit()
    print(f"Fyle name is {get_name(path)}")

    