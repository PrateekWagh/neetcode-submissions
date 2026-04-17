class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        c = collections.Counter(nums)
        heap = []
        output = []
        for key, value in c.items():
            heapq.heappush_max(heap, (value, key))
        for _ in range(k):
            output.append(heapq.heappop_max(heap)[1])
        return output    