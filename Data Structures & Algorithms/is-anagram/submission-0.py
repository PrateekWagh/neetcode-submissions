class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = collections.Counter(s)
        tHash = collections.Counter(t)
        if sHash == tHash:return True
        else:return False