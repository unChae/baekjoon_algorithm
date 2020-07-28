n = int(input())
line = 2*n-1

for i in range(line):
    res = ""
    if i < line/2:
        for j in range(i+1):
            res += "*"
    else:
        for j in range(line, i, -1):
            res += "*"
    print(res)