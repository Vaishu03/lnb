string = input()
length = len(string)
for i in range(length):
    if length>7 and i%2==0:
        print(string[i])
    elif length<=7 and i%2!=0:
        print(string[i])