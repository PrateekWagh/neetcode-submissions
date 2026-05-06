class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        vertices = {i:[] for i in range(n)}
        for u, v, w in flights:
            if u in vertices and v in vertices:
                vertices[u].append((v, w))
        pq = [(0, src, 0)]
        visited = {}
        while pq:
            cost, node, stops_used = heapq.heappop(pq)
            if node == dst:
                return cost
            if stops_used>k:continue
            if (node, stops_used) in visited and visited[(node, stops_used)]<=cost:
                continue
            visited[(node, stops_used)] = cost
            for neigh,price in vertices[node]:
                heapq.heappush(pq, (cost+price, neigh, stops_used+1))
        return -1