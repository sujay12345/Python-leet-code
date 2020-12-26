# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue=[root]
        nextqueue=[]
        level=[]
        result=[]
        while queue!= []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    nextqueue.append(root.left)
                if root.right is not None:
                    nextqueue.append(root.right)
            result.append(level)
            level=[]
            queue=nextqueue
            nextqueue=[]
        return result
        
        Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
