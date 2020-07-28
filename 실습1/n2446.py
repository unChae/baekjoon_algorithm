n = int(input())
line = 2*n-1

for i in range(line):
    if i >= n:
        i += 1
    res = ""
    for j in range(line):
        if i < line/2:
            if j < line-i:
                if j >= i:
                    res += "*"
                else:
                    res += " "
        else:
            if j >= line-i:
                if j < i:
                    res += "*"
            else:
                res += " "

    print(res)