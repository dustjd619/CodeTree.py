a,b = map(int,input().split())
count = [0] * 10
sum = 0

while True:
    count[a % b] += 1
    a = a // b

    if a//b <= 1:
        count[a % b] += 1
        break


for i in count:
    sum += i**2

print(sum)