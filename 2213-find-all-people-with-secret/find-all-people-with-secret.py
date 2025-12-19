class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = [[] for _ in range(n)]

        for meet in meetings:
            x, y, time = meet
            adj[x].append((time, y))
            adj[y].append((time, x))

        know = [float('inf')] * n
        people = []
        pq = []
        heapq.heappush(pq, (0, 0))
        heapq.heappush(pq, (0, firstPerson))
        while pq:
            time, person = heapq.heappop(pq)
            if know[person] != float('inf'):
                continue
            people.append(person)
            know[person] = time
            for t, neighbor in adj[person]:
                if know[neighbor] != float('inf') or t < time:
                    continue
                heapq.heappush(pq, (t, neighbor))
        return people