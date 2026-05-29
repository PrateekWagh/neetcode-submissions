class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def find(m, n, memo={}):
            if (m, n) in memo:return memo[(m, n)]
            if m == 0 or n == 0:return 0
            if m == 1 and n==1:return 1
            memo[(m, n)] = find(m-1, n, memo)+find(m, n-1, memo)
            return memo[(m, n)]
        return find(m, n)