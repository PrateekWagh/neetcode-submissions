class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, value in enumerate(nums):
            val = target-value
            if val not in table:
                table[value]= index
            else:return [table[val], index]    