from collections import deque
import math
graph = {}
graph[1] = {}
graph[2] = {}
graph[3] = {}
graph[4] = {}
graph[5] = {}
graph[6] = {}
graph[1][2] = 50
graph[1][3] = 45
graph[1][4] = 10
graph[2][4] = 15
graph[2][3] = 10
graph[3][5] = 30
graph[5][3] = 35
graph[4][1] = 10
graph[4][5] = 15
graph[5][2] = 20
graph[6][5] = 3
graph[3][6] = 10
print(graph)
visited = []
costs = {x:math.inf for x in range(1,7) }
costs[1]=0
parents = {1:None}
q = 1
def find_lowest(costs,visited):
    m = math.inf
    res = None
    for item in costs:
        if costs[item] < m and item not in visited:
            m = costs[item]
            res = item
    print(res)
    return res
while q:
    if q == 6:
        item = 6
        while item:
            print(item,end='->')
            item = parents[item]
        break
    visited.append(q)
    for child in graph[q]:
        if costs[child] > costs[q]+graph[q][child]:
            costs[child] = costs[q]+graph[q][child]
        print(costs)
    low = find_lowest(costs,visited)
    parents[low] = q
    q = low
