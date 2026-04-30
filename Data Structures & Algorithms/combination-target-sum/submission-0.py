class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def setCombination(target, nums, memo={}):
            nums.sort()
            key = (target, tuple(nums))
            if key in memo:
                return memo[key]
            if target <0:return []
            if target == 0:return [[]]    
            output = []
            for i, num in enumerate(nums):
                remainder = target - num
                result = setCombination(remainder, nums[i:], memo)
                for comb in result:
                    output.append([num]+comb)
            memo[key] = output
            return output
        return setCombination(target, nums)
