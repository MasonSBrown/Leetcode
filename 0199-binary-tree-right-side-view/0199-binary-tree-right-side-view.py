# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []
        if not root:
            return final
        q = deque([root])
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if i == l - 1:
                    final.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return final
            