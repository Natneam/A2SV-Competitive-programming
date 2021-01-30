# LINK TO THE PROBLEM =>  https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        indexOfMax = nums.index(max(nums))
        node = TreeNode(nums[indexOfMax])
        node.left = self.constructMaximumBinaryTree(nums[:indexOfMax])
        node.right = self.constructMaximumBinaryTree(nums[indexOfMax+1:])
        return node