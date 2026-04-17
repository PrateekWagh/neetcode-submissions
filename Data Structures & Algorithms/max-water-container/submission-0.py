class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        max_cap = 0
        while l<r:
            width = r-l
            length = min(heights[l], heights[r])
            cap = width*length
            max_cap = max(max_cap, cap)
            if heights[l]<heights[r]:
                l+=1
            else:r-=1
        return max_cap        