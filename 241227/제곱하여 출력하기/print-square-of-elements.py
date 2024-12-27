N = int(input())
a = list(map(int,input().split()))

for i in range(len(a)) :
    a[i] = a[i]*a[i]

for j in range(len(a)) :
    print(a[j],end=' ')