N = int(input())

if N % 5 == 0:
    for i in range(1,3):
        print(N*i,end=" ")

else:
    for i in range(1,11):
        print(N * i,end=' ')
