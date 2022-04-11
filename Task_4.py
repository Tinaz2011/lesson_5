my_list = [1, 1, 57, 46, 3, 5, 3, 76, 10, 2, 11, 11]
print("My list:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Elements with no repit:\n", new_list)