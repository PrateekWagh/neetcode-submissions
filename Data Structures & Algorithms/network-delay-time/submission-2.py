class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        vertices = {i:[] for i in range(1, n+1)}
        for u, v, w in times:
            if u in vertices and v in vertices:
                vertices[u].append((v, w))
        previous = {node:None for node in vertices.keys()}
        time_table = {node:float("inf") for node in vertices.keys()}
        time_table[k]= 0
        heap = [(0, k)]
        while heap:
            curr_time, curr_node = heapq.heappop(heap)
            if time_table[curr_node]<curr_time:
                continue
            for neigh, time in vertices[curr_node]:
                total_time = curr_time+time
                if total_time<time_table[neigh]:
                    previous[neigh] = curr_node
                    time_table[neigh] = total_time
                    heapq.heappush(heap, (total_time, neigh))
        print(previous)
        print(time_table)
        if max(time_table.values()) == float("inf"):
            return -1
        else:
            return max(time_table.values())  