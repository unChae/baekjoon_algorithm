T = int(input())
P = ""
for i in range(T):
    R, S = map(str, input().split())
    for j in range(len(S)):
        for z in range(int(R)):
            P += S[j] 
    P += "\n"
print(P)   