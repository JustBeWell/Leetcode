# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
          return []

        sol = []
        q = deque([root])
        sol.append([root.val])
        while q:
          for i in range(len(q)):
            node = q.popleft()
            if node.left:
              q.append(node.left)
            if node.right:
              q.append(node.right)

          if len(q) != 0:
            level_list = []
            for i in q:
              level_list.append(i.val)
            sol.append(level_list)   

        return sol