m = int(input("Максимальная масса: "))
n = int(input("Количество рыбаков: "))
res = []
if ((m >= 1 and m <= 10 * (10 ** 6)) 
    and (n >= 1 and n <= 100)):
    for i in range(n):
        weight = int(input(f"Введите вес {i+1} рыбака: "))
        if weight >= 1 and weight <= m: 
            res.append(weight)
        else:
            print("Введен недопустимый вес. 1<=Ai<=m")
            exit()
    res.sort()
    count = res.count(m)
    for i in range(len(res)-1):
        for j in range(i+1, len(res)):
            if (res[j] + res[i] > m) and (res[j-1] + res[i] <= m):
                count += 1
                break
    print(f"Нужно лодок: {count}")
else:
    print("Введены недопустимые значения. 1<=m<=10e6, 1<=n<=100")