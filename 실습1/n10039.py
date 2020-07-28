total_score = 0
aver = 0

for i in range(5):
    score = int(input())
    if score <= 40:
        total_score = total_score + 40
    else:
        total_score = total_score + score
aver = int(total_score/5)
print(aver)
