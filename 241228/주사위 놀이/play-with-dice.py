dice = list(map(int, input().split()))
count=[0]*6

for i in dice:
    if i in dice:
        count[i-1] += 1

for j in range(1,7):
    print('%d - %d'%(j,count[j-1]))
