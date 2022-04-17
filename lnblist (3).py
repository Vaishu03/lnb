my_list = [x for x in range(1,21)]
new_list = []
new_list.extend(my_list[:5])
new_list.extend(my_list[15:])
other_list = [x**2 for x in new_list]
part_1 = other_list[:2]
part_2 = other_list[2:5]
part_3 = other_list[5:]
print(part_1)
print(part_2)
print(part_3)