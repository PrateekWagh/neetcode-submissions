class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        perm = itertools.permutations(nums)
        output = []
        for item in perm:
            output.append(list(item))
        return output