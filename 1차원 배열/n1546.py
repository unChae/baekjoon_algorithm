n = int(input())
score_list = list(map(int, input().split()))
max = score_list[0]

# 최댓값
for i in score_list:
  if i > max:
    max = i

for i in range(n):
  score_list[i] = score_list[i]/max*100

sum = 0
aver = 0
for i in range(n):
  sum += score_list[i]
  aver = float(sum/n)

print(aver)