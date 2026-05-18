class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        output = []
        for i in range(len(nums)):
            output.append(heapq.heappop(nums))
        return output