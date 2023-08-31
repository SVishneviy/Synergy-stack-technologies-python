print("Введите слово на латинице:")
str = input().lower()
str1 = str.translate({ord('a') : None, ord('e') : None, ord('i') : None, ord('o') : None, ord('u') : None})
print(f"Количество гласных: {str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')}")
print(f"Количество согласных: {len(str1)}")
if (str.find("a") != -1 and 
    str.find("e") != -1 and 
    str.find("i") != -1 and 
    str.find("o") != -1 and 
    str.find("u") != -1):
    print(f"Количество a: {str.count('a')}")
    print(f"Количество e: {str.count('e')}")
    print(f"Количество i: {str.count('i')}")
    print(f"Количество o: {str.count('o')}")
    print(f"Количество u: {str.count('u')}")
else:
    print(False)