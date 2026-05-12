class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        output = []
        for item in strs:
            d[tuple(sorted(item))].append(item)
        for value in d.values():
            output.append(value)
        return output