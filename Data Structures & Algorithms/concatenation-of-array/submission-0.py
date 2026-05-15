class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsT = nums.copy()
        for item in numsT:
            nums.append(item)
        return nums