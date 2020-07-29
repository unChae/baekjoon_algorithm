array = [i for i in range(1, 10001)]
for i in range(1, 10000):
    sum = i
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    try:
        array.remove(sum)
    except:
        continue

for i in array:
    print(i)

