import heapq
from collections import defaultdict

class Solution:
    def processQueries(self, c, connections, queries):
        parent = list(range(c+1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for u,v in connections:
            union(u,v)

        comp_heap = defaultdict(list)
        for node in range(1, c+1):
            r = find(node)
            heapq.heappush(comp_heap[r], node)

        online = [True] * (c+1)
        ans = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    ans.append(x)
                else:
                    r = find(x)
                    heap = comp_heap[r]
                    while heap and not online[heap[0]]:
                        heapq.heappop(heap)
                    ans.append(heap[0] if heap else -1)
            else:
                if online[x]:
                    online[x] = False
        return ans
