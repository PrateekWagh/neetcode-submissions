class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        c = collections.Counter(nums)
        for key, value in c.items():
            if value>(len(nums)//3):
                output.append(key)
        return output