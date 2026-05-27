class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        output = []
        c = collections.Counter(nums)
     
        nums.sort(key=lambda x:(c[x], -x))
        return nums
            