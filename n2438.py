n = int(input())
for i in range(n):
    res = ""
    for j in range(i+1):
        res = res+"*"
    print(res)