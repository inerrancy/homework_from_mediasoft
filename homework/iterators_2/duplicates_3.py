d_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 7, 2, 5, 8, 9, 7, 7]
print(d_list)
list = []
[list.append(i) for i in d_list if i not in list]
print(list)