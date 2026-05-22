# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # get the heights of each node
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            
            if left == -1 or right == -1:
                return -1

            elif abs(left-right) > 1:
                return -1

            else:
                return max(left, right) +1

        balanced = dfs(root)
        if balanced == -1:
            return False
        return True

