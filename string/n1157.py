S = input()
S = S.upper()
array = [chr(i) for i in range(65, 91)]
max = 0
for i, v in enumerate(array):
    temp = v
    count = 0
    for j in range(len(S)):
        if S[j] == v:
            count += 1
    if max < count:
        max = count
        result = v
    elif max == count:
        result = "?"

print(result)