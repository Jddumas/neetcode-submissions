# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightside = []
        q = deque()
        q.append(root)
        while q:
            
            level_length = len(q)
            for i in range(level_length):
                cur = q.popleft()
                if i == level_length - 1:
                    rightside.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return rightside

        