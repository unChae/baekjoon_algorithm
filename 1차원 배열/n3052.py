number_list = []
for i in range(10):
  number_list.append(int(input()))

# 그냥 배열 중복제거 만들어 본 것
temp_list = []

for i in number_list:
  temp_list.append(i%42)

for i in range(len(temp_list)-1):
  for j in range(i+1, len(temp_list)):
    if(temp_list[i] == temp_list[j]):
      temp_list[j] = -1

count = 0
for i in temp_list:
  if i != -1:
    count += 1

print(count)

# list set 사용한 방법
temp_list = []
for i in number_list:
  temp_list.append(i%42)

print(len(list(set(temp_list))))

