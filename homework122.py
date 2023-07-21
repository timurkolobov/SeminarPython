#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки.
#Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

def findNumbers(S, P):
    # Найдем все возможные пары чисел X и Y
    for X in range(1, 1001):
        for Y in range(1, 1001):
            # Проверим, что сумма и произведение совпадают
            if X + Y == S and X * Y == P:
                return X, Y
                
    return None

# Введите сумму и произведение, которые Петя назвал
S = int(input("Введите сумму: "))
P = int(input("Введите произведение: "))

# Найдем числа X и Y
numbers = findNumbers(S, P)

if numbers:
    print("Числа X и Y:", numbers)
else:
    print("Числа не найдены.")