class1 = int (input("Введите кол-во учащихся 1го класса: "))
class2 = int (input("Введите кол-во учащихся 2го класса: "))
class3 = int (input("Введите кол-во учащихся 3го класса: "))

tables = (class1+1)//2 + (class2+1)//2 + (class3+1)//2
print(tables)
