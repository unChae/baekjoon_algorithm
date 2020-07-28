n = int(input())
number_list = list(map(int, input().split()))
max = number_list[0]
min = number_list[0]

for i in number_list:
    if max < i:
        max = i
    if min > i:
        min = i

print(min,max)