class Solution:
    def isValid(self, s: str) -> bool:
        table = {")":"(", "}":"{", "]":"["}
        stack = []
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif stack and stack[-1] == table[bracket]:stack.pop()
            else:return False
        if stack:return False 
        else: return True