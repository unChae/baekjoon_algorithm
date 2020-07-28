number_list = []
max = 0
temp = 0
for i in range(9):
    number_list.append(int(input()))

for i, v in enumerate(number_list):
    if v > max:
        max = v
        temp = i

print(max)
print(temp+1)