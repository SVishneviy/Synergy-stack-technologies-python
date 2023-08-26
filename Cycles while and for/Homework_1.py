n = int(input("Введите число n: "))
count = 0
while n > 0:
    num = int(input("Введите число: "))
    if num == 0:
        count += 1
    n -= 1
print(f"Количество нулей: {count}")