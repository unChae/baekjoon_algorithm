import sys
 
a,b = map(int, sys.stdin.readline().split())
c = list(map(int, input().split()))

res = ""
for i in range(a):
    if(b > c[i]):
        res = res+str(c[i])+" "

print(res)
