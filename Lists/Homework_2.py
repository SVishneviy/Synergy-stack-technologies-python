n = int(input("Введите длину списка: "))
res = []
if n >= 1 and n <= 100000:
    temp = list(map(int, input("Введите числа через пробел, соблюдая условие 1<=1Ai<=10e9, "
                               "иначе элемент будет удален:\n").split()))[:n]
    res = list(int(x) for x in temp if x >= 1 and x <= 10 * (10 ** 9))
    if(len(res) > 0):
        res.insert(0, res.pop())
        print(res)
    else:
        print("Массив пустой")