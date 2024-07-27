class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)    #defualt value is list
        for src, dst, cur_cost in zip(original, changed, cost): #zip all three arrays
            adj[src].append((dst, cur_cost)) #tuple
        
        def dijkstra(src):
            heap = [(0, src)]
            min_cost_map = {}
            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map:
                    continue #skip
                min_cost_map[node] = cost
                for nei, nei_cost in adj[node]:
                    heapq.heappush(heap, (cost + nei_cost, nei))
            return min_cost_map
        
        min_cost_maps = {c:dijkstra(c) for c in set(source)}
        res = 0
        for src, dst, in zip(source, target):
            if dst not in min_cost_maps[src]:
                return -1
            res += min_cost_maps[src][dst]
        return res



        
            
            
