# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        node_list = []
        tulist = []

        def dfs(node, depth):
            if not node:
                return None
            if len(node_list) == depth:
                node_list.append([])
            
            node_list[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 0)
        for i in range(len(node_list)):
            tulist.append(node_list[i][-1])
        return tulist