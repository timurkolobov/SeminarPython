n = int(input('Введите кол-во дней'))
i = 0
count = 0
max = 0
while i < n:
    temp = int(input("Введите температуру: "))
    if temp > 0:
        count += 1
        if count > max:
            max = count
    else:
        count = 0
    i += 1
print(max)