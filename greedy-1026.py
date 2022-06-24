import sys

n = int(sys.stdin.readline())
aryA = list(map(int, sys.stdin.readline().split()))
aryB = list(map(int, sys.stdin.readline().split()))
sum = 0

aryA.sort()
aryB.sort(reverse = True)

for i in range(0, n):
    sum += aryA[i] * aryB[i]

print(sum)

