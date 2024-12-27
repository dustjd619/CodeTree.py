n = int(input())
num = [1,n]

while True:
    a = num[-2] + num[-1]
    num.append(a)

    if a > 100:
         break

for i in num:
    print(i,end=" ")