while True:
    n = int(input('Введите кол-во арбузов -> '))
    if n > 1:
        break
max_weight = int(input(f'Введите вес арбуза {n} ->'))
min_weight = int(input(f'Введите вес арбуза {n - 1} ->'))

while n -2 > 0:
    temp = int(input(f'Введите вес арбуза {n - 2} -> '))
    if min_weight > temp:
        min_weight = temp
    if max_weight < temp:
        max_weight = temp
    n -= 1

print(f'Ваш арбуз весит {max_weight} кг'
      f'а арбуз для тещи весит {min_weight} кг')