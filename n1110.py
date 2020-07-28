import math
n = int(input())

def fir(n):
    return int(n/10)

def sec(n):
    if(n == 1):
        return 1
    return int(n%10)

count = 0
temp = n
check = False

while True:
    temp = int(temp)

    sum = fir(temp) + sec(temp)

    if(temp == n and check == True):
        break
    
    if(sum >= 10):
        temp = str(sec(temp)) + str(sec(sum))
    else:
        temp = str(sec(temp)) + str(sum)
    print(temp)
    check = True
    count = count + 1
    
print(count)