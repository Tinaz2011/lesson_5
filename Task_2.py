result_list = []
list = [int(i) for i in input("input your list: ").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("your list: ", list)
print("Elements that are bigger then privious: ", result_list)