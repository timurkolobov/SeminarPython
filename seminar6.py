A = 8
num1 = 0
num2 = 1
series = 0
s = 0
while s<= A:
    s = s+1
    if (A == series):
        print(s)
        break
    num1 = num2
    num2 = series
    series = num1 + num2
else: print("-1")

