num = list(map(int,input().split()))

for i in range(3,11):
    a = num[-1] + num[-2]
    if a // 10 == 0 :
        num.append(a)
    else : 
        a = a %10
        num.append(a)

for j in range(len(num)):
    print(num[j],end=" ")