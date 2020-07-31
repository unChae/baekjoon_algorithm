import sys
N = int(sys.stdin.readline())
a = [0 for i in range(N)]
for i in range(N-1):
    u, v, c = map(int, sys.stdin.readline().split())
    a[u] += 1    
    a[v] += 1
index = a.index(max(a))
print(a)