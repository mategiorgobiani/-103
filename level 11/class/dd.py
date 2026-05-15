
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)


my_list.append(11)
my_list.append(12)
my_list.append(13)
my_list.append(14)

print(my_list)


my_list.pop(0)
my_list.pop(0)

print(my_list)


print(my_list.count(5))


my_list.reverse()

print(my_list)


my_list.sort(reverse=True)

print(my_list)


list2 = [100, 200, 300]

new_list = my_list + list2

print(new_list)

copy_list = new_list.copy()

print(copy_list)


new_list.clear()

print(new_list)


