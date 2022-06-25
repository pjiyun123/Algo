import sys

a = sys.stdin.readline().split('-')
sum = 0
num = []

for i in a:
    cnt = 0
    b = i.split('+')
    for j in b:
        cnt += int(j)
    num.append(cnt)

sum = num[0]
for i in range(1, len(num)):
    sum -= num[i]

print(sum)

 
