# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            # base case
            if not node:
                return 0
            
            # run the dfs
            left = dfs(node.left)
            right = dfs(node.right)

            # get the diameter
            self.res = max(self.res, left+right)

            # recurse up
            return 1 + max(left, right)

        dfs(root)

        return self.res




        