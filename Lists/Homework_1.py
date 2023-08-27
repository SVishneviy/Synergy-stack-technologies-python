n = int(input("Введите длину списка: "))
res = []
if n >= 1 and n <= 10000:
    while n > 0:
        num = int(input("Введите число: "))
        if abs(num) < 10 * (10 ** 5):
            res.append(num)
            n -= 1
        else:
            print("Число превышает 10e5")
    print(res)
    res.reverse()
    print(res)
else:
    print("Не допустимая длина списка (1<=N<=10000)")