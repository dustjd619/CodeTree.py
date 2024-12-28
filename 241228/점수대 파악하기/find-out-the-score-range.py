score = list(map(int,input().split()))
count = [0] * 10

for i in score:
    if i // 10 > 0:
        count[10- i//10] += 1
    elif i == 0:
        break

for j in range(10):
    print("%d - %d" %(100-j*10,count[j]))