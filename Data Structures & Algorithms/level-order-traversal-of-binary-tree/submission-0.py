# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dq = collections.deque([root])
        output = []
        while dq:
            qlen = len(dq)
            level = []
            for i in range(qlen):
                node = dq.popleft()
                if node:
                    level.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if level:
                output.append(level)        
        return output