n = int(input("Введите количество чисел: "))
res = list(map(int, input("Введите числа через пробел не превышающие 2*10e9, "
                          "иначе элемент будет удален:\n").split()))[:n]
res = list(int(x) for x in res if abs(x) < 2 * (10 ** 9))
print(len(set(res)))