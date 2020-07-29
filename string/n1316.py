N = int(input())
a = []
for i in range(N): 
    a.append(input())
count = 0
for i in a:
    ta = []
    check = True
    for j in i:
        if len(ta) < 1:
            ta = j
        else:
            for z in ta:
                if z == j:
                    check = False
                else:
                    ta.append(j)
        print(ta)
    if check:
        count += 1

print(count)