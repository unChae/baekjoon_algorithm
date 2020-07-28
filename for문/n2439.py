n = int(input())
for i in range(n):
    res = ""
    for j in range(n):
        if(j > (n-i-2)):
            res = res+"*"
        else:
            res = res+" "
    print(res)