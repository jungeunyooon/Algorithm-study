import sys
import heapq

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

edge = [sys.maxsize] * (v + 1)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    edge[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if edge[now] < dist:
            continue

        for i in graph[now]:
            cost = edge[now] + i[1]

            if cost < edge[i[0]]:
                edge[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(k)

for i in range(1, v + 1):
    if edge[i] == sys.maxsize:
        print("INF")
    else:
        print(edge[i])