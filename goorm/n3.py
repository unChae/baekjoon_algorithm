#숫자 카드 게임

import sys
import itertools

N, M = map(int, sys.stdin.readline().split())
S = ""
asn = 0
for i in range(N):
    S += str(i)
A = list(itertools.combinations(S, M))
for i in A:
    C = 0
    for j in i:
        C += int(j)
    if(C%N == 0):
        asn += 1
print(asn)

