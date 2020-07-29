C = int(input())
array = []
for i in range(C):
    array.append(list(map(int, input().split())))

for i in array:
    sum = 0
    aver = 0
    #평균 구하기
    for index, j in enumerate(i):
        if index != 0:
            sum += j
    aver = sum/i[0]
    #평균 보다 높은 애들
    count = 0
    for index, j in enumerate(i):
        if index != 0:
            if(aver < j):
                count += 1
    result = round(count/i[0]*100, 3)
    print(format(result,".3f")+"%")
    
