# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global good
        maxode = root.val
        good = 0
        
        self.dfs(root, maxode)
        return good
    
    def dfs(self, root, maxode):
        global good
        if not root:
            return None

        if root.val >= maxode:
            good += 1
        maxode = max(maxode, root.val)

        self.dfs(root.left, maxode)
        self.dfs(root.right, maxode)

            
