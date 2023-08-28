def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact        

n = int(input("Введите натуральное целое число: "))
if n > 0:
    n = factorial(abs(n))
    res = []
    for i in range(1, n+1):
        res.append(factorial(i))
    print(list(reversed(res)))
else:
    print("Неверное значение")