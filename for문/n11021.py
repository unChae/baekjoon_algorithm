import sys
 
inp = int(input())
j = 0
for i in range(inp):
    j = j+1
    a,b = map(int, sys.stdin.readline().split())
    print("Case #"+str(j)+":",a+b)
