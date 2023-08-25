print("Введите число:")
num = int(input())
parity = "четное"
if num % 2 != 0:
    parity = "нечетное"
    print("Число не является четным")
if num < 0:
    print("Отрицательное %s число" %parity)
elif num > 0:
    print("Положительное %s число" %parity)
else:
    print("Нулевое число")