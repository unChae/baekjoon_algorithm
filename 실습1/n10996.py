n = int(input())
line = n*2

for i in range(line):
    res = ""
    if n == 1:
        print("*")
        break
    switch = False
    if i%2 == 0:
        switch = True
    else:
        switch = False

    for j in range(line):
        if j == n:
            break
        if switch:
            if j%2==0:
                res += "*"
            else:
                res += " "
        else:
            if j%2==0:
                res += " "
            else:
                res += "*"
    print(res)