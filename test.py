import heapq
import sys
input = sys.stdin.readline

N, M, A, B, C = map(int,input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

arrived = False

visited = set([A])
q = []

q.append((0, 0, A, visited))

while q:
    shame, t_c, now, n_visited= heapq.heappop(q)

    if now == B:
        arrived = True
        Shame = shame
        break

    for next, cost in graph[now]:
        if next in n_visited:
            continue
        if t_c + cost > C:
            continue
        
        heapq.heappush(q, (max((shame, cost)), t_c + cost, next, n_visited|set([next])))
        print(list(q))

if arrived:
    print(Shame)

else:
    print(-1)

'''
5 5 1 5 10
1 2 5
1 3 1
2 4 2
3 4 6
4 5 1

'''