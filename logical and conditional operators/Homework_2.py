print("Введите слово на латинице:")
str = input().lower()
if (str.find("a") != -1 
    and str.find("e") != -1 
    and str.find("i") != -1 
    and str.find("o") != -1 
    and str.find("u") != -1):
    print("Количество a: %s" %str.count("a"))
    print("Количество e: %s" %str.count("e"))
    print("Количество i: %s" %str.count("i"))
    print("Количество o: %s" %str.count("o"))
    print("Количество u: %s" %str.count("u"))
else:
    print(False)