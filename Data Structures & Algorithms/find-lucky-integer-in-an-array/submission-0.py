class Solution:
    def findLucky(self, arr: List[int]) -> int:
        max_val = 0
        counter = collections.Counter(arr)
        output = -1
        for key, value in counter.items():
            if key == counter[key] and key>max_val:
                max_val = key
                output = key
        return output