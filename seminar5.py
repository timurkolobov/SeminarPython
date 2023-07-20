a = 5
fib = 1
sum = 0
count = 0
while fib <= a:
    sum = fib
    fib += sum
    count += 1
    print(fib)
print(count)
