# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # flip left and right children
        if not root:
            return None

        tmpright = root.right
        tmpleft = root.left

        root.right = tmpleft
        root.left=tmpright

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
         
        