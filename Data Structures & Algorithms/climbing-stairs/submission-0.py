class Solution:
    def climbStairs(self, n: int) -> int:
        def ways(value, memo={}):
            if value in memo:return memo[value]
            if value==0:return 1
            if value<0:return 0
            memo[value] = ways(value-1, memo)+ways(value-2, memo)
            return memo[value]   
        return ways(n)
