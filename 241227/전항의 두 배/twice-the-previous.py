num = list(map(int,input().split()))

for i in range(2,10):
    a = num[-1] + 2 * num[-2]
    num.append(a)

for j in range(len(num)):
    print(num[j],end=" ")