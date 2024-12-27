num = list(map(int,input().split()))
res =[]

for i in num:
    if i % 2 == 0 and i != 0:
        i = i // 2
        res.append(i)
    elif i % 2 != 0:
        i = i + 3
        res.append(i)
    else:
        break
    
for j in range(len(res)):
    print(res[j],end=" ")