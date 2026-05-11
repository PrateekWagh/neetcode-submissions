class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        k = 2
        i = 0
        j = 1
        while j<len(nums):
            if nums[i]==nums[j]:return True
            else:
                j+=1
                i+=1
        return False