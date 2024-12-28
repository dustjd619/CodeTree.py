count =[0] * 5

for _ in range(3):
    c, t = input().split()
    t = int(t)
    if c == 'Y' and t >= 37:
        count[0] += 1
    elif c == 'N' and t >= 37:
        count[1] += 1
    elif c == 'Y' and t<37:
        count[2] += 1
    else:
        count[3] += 1

if count[0] >= 2 :
    count[4] = 'E'
else :
    count.pop(4)

for i in count:
    print(i, end=" ")