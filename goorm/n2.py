#사은품 교환하기
import sys

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())

    k1 = N/5
    k2 = (N+M)/12

    if k1 < k2:
        k = k1
    else:
        k = k2
        
    while N+M < 12*k:
        if k == 0: 
            break
        k -= 1
    sys.stdout.write(str(int(k))+"\n")

    

