n = int(input())
array = []
for i in range(n):
  array.append(input())

for i in array:
  count = 0
  conti = 1
  result = 0
  for j in i:
    if j == "O":
      count = 1*conti
      conti += 1
      result += count
    else:
      count = 0
      conti = 1
    
  print(result)