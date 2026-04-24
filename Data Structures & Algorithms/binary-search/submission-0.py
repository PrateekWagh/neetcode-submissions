class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(low, high, target, arr):
            mid = (low+high)//2
            if low<=high:
                if arr[mid]<target:
                    return binary(mid+1, high, target, arr)
                elif arr[mid]>target:
                    return binary(low, mid-1, target, arr)
                else:return mid
            else:return -1
        return binary(0, len(nums)-1, target, nums)        