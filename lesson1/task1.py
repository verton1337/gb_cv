n = input("Введите N: ")
try:
    n = int(n)
except ValueError:
    print("Введено некорректное значение")
    exit()
for i in range(1,n+1):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")
    print("_"*10)