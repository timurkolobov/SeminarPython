n = int(input('Введите число -> '))
if n == 0:
    print(1)
else:
    frst, scnd, count = 0, 1, 2
    while scnd <= n:
        if scnd == n:
            print(count)
            break
        frst, scnd = scnd, frst + scnd
        count += 1
    else:
        print(-1)
