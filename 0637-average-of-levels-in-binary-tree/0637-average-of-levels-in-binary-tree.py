class Solution:
    from collections import deque
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        final = []
        if not root:
            return []
        q = deque([root])
        print(q)
        while q:
            l = len(q) #level size
            s = 0 #should be sum of level
            for i in range(l):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            avg = s / l
            final.append(avg)
        return final
        
            

        