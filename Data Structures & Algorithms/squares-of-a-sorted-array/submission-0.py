class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output =[]
        for item in nums:
            output.append(item**2)
        output.sort()
        return output        