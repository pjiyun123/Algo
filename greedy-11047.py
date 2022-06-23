import sys

n, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
count = 0

for i in range(n-1, -1, -1):
    if(k == 0):
        break;
    if(k >= arr[i]):
        count += k // arr[i]
        k = k % arr[i]

print(count)
