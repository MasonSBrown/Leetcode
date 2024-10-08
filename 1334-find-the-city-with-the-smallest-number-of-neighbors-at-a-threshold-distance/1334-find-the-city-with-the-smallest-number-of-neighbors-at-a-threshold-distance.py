class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        #sets up blueprint
        for v1, v2, dist in edges:
            #sets it up as a tuple
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def dijkstra(src): #dijkstra's algorithm** important #greedy
            heap = [(0, src)] #dist, node
            visit = set()
            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))
            return len(visit) - 1
        
        result, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                result, min_count = src, count
        return result