num = list(map(int, input().split()))

num.remove(num[-1])

print(max(num), min(num))