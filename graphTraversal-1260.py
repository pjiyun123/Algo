import sys
from collections import deque

node, edge, start = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(node+1)] for _ in range(node+1)]
visit_dfs = [0] * (node+1)
visit_bfs = [0] * (node+1)

for i in range(0, edge):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


def dfs(start):
    visit_dfs[start] = 1
    print(start, end = " ")
    for i in range(1, node+1):
        if visit_dfs[i] == 0 and graph[start][i] == 1:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visit_bfs[start] = 1
    while q:
        start = q.popleft()
        print(start, end = " ")
        for i in range(1, node+1):
            if visit_bfs[i] == 0 and graph[start][i] == 1:
                q.append(i)
                visit_bfs[i] = 1

dfs(start)
print()
bfs(start)
