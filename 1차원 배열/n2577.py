import math

A = int(input())
B = int(input())
C = int(input())

multi = A * B * C
result = [0,0,0,0,0,0,0,0,0,0]
for i in range(len(str(multi))):
    i += 1
    char = math.trunc((multi - (math.trunc(multi/10**i)*10**i))/10**(i-1))

    result[char] += 1


for i in result:
    print(i)
