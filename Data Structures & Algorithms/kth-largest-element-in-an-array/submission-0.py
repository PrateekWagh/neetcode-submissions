class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        output = []
        for item in nums:
            heapq.heappush(heap, -item)
        for i in range(len(heap)):
             output.append(heapq.heappop(heap))
        return output[k-1]*-1