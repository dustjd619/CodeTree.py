n = int(input())
a = list(map(int, input().split()))

# Write your code here!
b = sorted(a)

count = 0
for i in b:
    if b[0] != i:
        break
    count += 1
    
print(b[0], count)