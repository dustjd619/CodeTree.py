n = int(input())
num = list(map(int,input().split()))
count = [0] * 9

for i in num:
    if i in num:
        count[i-1] += 1

for j in  count:
    print(j)