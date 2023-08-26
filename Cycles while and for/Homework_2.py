x = int(input("Введите число: "))
count = 0
if x <= 2 * (10 ** 9):
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    print(f"Количество натуральных делителей: {count}")
else:
    print("X > 2e9")