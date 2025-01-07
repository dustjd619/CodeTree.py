n, m = map(int,input().split())
num = list(map(int,input().split()))
count = 0

for i in range(len(num)):
    if num[i] == m:
        count += 1

print(count)
    