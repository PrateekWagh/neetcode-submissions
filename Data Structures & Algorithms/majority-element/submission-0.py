class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for key, value in counter.items():
            if counter[key]>(len(nums)//2):
                return key