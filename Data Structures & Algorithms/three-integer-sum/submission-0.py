class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for index, value in enumerate(nums):
            if index>0 and nums[index-1] == value:
                continue
            l, r = index+1, len(nums)-1
            while l<r:
                threesum = value+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([value, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res                            