n = int(input())
num = list(map(int,input().split()))
count = 0
index = 0

for i in num:
    if i == 2:
        count += 1
        if count == 3:
            index += 1
            print(index)
    index += 1