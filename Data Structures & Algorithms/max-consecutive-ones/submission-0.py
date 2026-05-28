class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        max_ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                total+=1
            else:
                max_ones = max(max_ones, total)
                total=0
        return max_ones if max_ones>total else total