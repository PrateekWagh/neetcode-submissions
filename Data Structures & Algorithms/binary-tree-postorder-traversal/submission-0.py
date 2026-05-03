# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
         def postorder(root, items):
            if root:
                
                postorder(root.left, items)
                postorder(root.right, items)
                items.append(root.val)
            return items
         return postorder(root, [])