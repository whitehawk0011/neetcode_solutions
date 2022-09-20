# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mmax = sys.maxsize
        mmin = -mmax
        return Solution.browseTree(root,mmin,mmax)
        
    
    def browseTree(root,mmin,mmax):
        if root == None :
            return True
        else:
            if root.val > mmin and root.val < mmax:
                L = Solution.browseTree(root.left,mmin,root.val)
                R = Solution.browseTree(root.right,root.val,mmax)
                return (L and R)
            else :
                return False
        # https://leetcode.com/problems/validate-binary-search-tree/
