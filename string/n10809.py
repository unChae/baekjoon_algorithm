S = input()
array = [i for i in range(97, 123)]

for j, v in enumerate(array):
    temp = v
    for i in range(len(str(S))):
        if ord(S[i]) == v:
            array[j] = i
            break
    if temp == array[j]:
        array[j] = -1
result = ""
for i in array:
    result += str(i) + " "
print(result)