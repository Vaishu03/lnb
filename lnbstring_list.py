string = input().split()
res = []
for i in range(len(string)):
    if len(string[i])>4:
        res.append(string[i])
print(res)