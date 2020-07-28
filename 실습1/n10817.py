input_list = list(map(int,input().split()))

for i, v in enumerate(input_list):
    for j, v in enumerate(input_list):
        if j+1 == 3:
            break
        if input_list[j] > input_list[j+1]:
            temp = input_list[j]
            input_list[j] = input_list[j+1]
            input_list[j+1] = temp
        
print(input_list[1])