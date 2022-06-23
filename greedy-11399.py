import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
wait = 0

arr.sort()
for i in range(0, n):
    wait += int(arr[i]) * (n-i)

print(wait)
