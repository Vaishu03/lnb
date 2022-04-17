inp_tuple = tuple(map(int,input().split()))
inp_str = input()
conv_list = []
for i in range(len(inp_tuple)):
    conv_list.append(inp_tuple[i])
    conv_list.append(inp_str)
print(tuple(conv_list))
