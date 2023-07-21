#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def print_powers_of_two(n):
    power = 0
    result = []
    while 2 ** power <= n:
        result.append(2 ** power)
        power += 1
    return result

N = int(input("Введите число N: "))
powers = print_powers_of_two(N)
print("Целые степени двойки, не превосходящие число", N, ":", powers)
