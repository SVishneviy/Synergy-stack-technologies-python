def print_list(list):
    if not list:
        print("Конец списка")
    else:
        print(list[0])
        print_list(list[1:])
        
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print_list(my_list)
