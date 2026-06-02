class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
       
        def find(m, n):
            if m>=len(grid) or n>=len(grid[0]):
                return float("inf")
            if (m, n) in memo:
                return memo[(m, n)]
            if m == len(grid)-1 and n==len(grid[0])-1:
                return grid[m][n]
            memo[(m, n)]= grid[m][n] + min(
                find(m + 1, n),
                find(m, n + 1)
            )    
            return memo[(m, n)]
        return find(0, 0)