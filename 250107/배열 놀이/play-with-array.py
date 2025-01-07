n,q = map(int,input().split())
num = list(map(int,input().split()))

for _ in range(q):
    ex = list(map(int,input().split()))

    if ex[0] == 1:
        print(num[ex[1]-1])

    elif ex[0] == 2:
        if ex[1] in num:
            print(num.index(ex[1])+1)
        else:
            print(0)

    else:
        for i in range(ex[1]-1,ex[2]):
            print(num[i], end=" ")
        print()
