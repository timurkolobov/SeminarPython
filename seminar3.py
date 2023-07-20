year = int(input('Введите год: '))
if year%4 == 0:
    if year%400 == 0:
        print('yes')
    elif year%100 == 0:
        print('no')
    else: print('Yes')
else: print('no')