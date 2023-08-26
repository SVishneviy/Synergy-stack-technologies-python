a, b = map(int, input("Введите числa A и B: ").split())
if a <= b:
    for i in range(a, b + 1):
        if a % 2 == 0:
            print(a, end=" ")
        a += 1
else:
    print("Неверное условие: A > B")