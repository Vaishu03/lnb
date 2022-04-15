my_list = []
for _ in range(5):
    num = int(input())
    if num>=9:
        my_list.append(num)
print(sum(my_list))