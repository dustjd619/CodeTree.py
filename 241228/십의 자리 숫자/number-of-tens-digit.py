num = list(map(int,input().split()))
count = [0]*9

for i in num :
    if i // 10 > 0:
        count[i // 10 - 1] += 1
    elif i == 0:
        break

for j in range(1,10):
    print("%d - %d"%(j,count[j-1]))