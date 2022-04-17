L1 = [11,21,24,12,18]
L2 = [14,44,25,37,13]
L3 = []
for i in range(len(L1)):
    if i%2==0:
        L3.append(L1[i])
for j in range(len(L2)):
    if j%2!=0:
        L3.append(L2[j])
print(L3)