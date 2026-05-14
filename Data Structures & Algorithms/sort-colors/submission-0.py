class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros=ones=twos=0
        for item in nums:
            if item==0:zeros+=1
            if item==1:ones+=1
            if item==2:twos+=1
        for i in range(len(nums)):
            if zeros>0:
                nums[i]=0
                zeros-=1
            elif ones>0:
                nums[i]=1
                ones-=1
            else:
                nums[i]=2
                twos-=1