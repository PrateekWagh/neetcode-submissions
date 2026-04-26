class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        j = k
        output = []
        while j<len(nums)+1:
            res = max(nums[i:j])
            output.append(res)
            i+=1
            j+=1
        return output    