class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = collections.Counter(nums)
        for key, value in c.items():
            if value>=2:return True
        return False