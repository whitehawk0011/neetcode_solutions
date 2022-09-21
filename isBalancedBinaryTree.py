# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        lh = Solution.findHeight(root.left)
        rh = Solution.findHeight(root.right)
        if abs(lh-rh) <2 and Solution.isBalanced(self,root.left) and Solution.isBalanced(self,root.right):
            return True
        else:
            return False
    def findHeight(root):
        if root is None:
            return 0
        return max(Solution.findHeight(root.left), Solution.findHeight(root.right)) + 1

    #https://leetcode.com/problems/balanced-binary-tree/submissions/
