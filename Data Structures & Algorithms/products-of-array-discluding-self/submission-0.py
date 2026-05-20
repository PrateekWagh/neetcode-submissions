class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 0
        right=0
        output = []
        product=1
        while left<len(nums):
            while right<len(nums):
                if left!=right:
                    product*=nums[right]
                right+=1
            output.append(product)
            left+=1
            right=0
            product=1
        return output
            