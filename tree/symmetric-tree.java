/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSymmetric(TreeNode root) 
    {
        if (root == null)
        {
            return true;
        }

        return sameSame(root.left, root.right);
    }

    public boolean sameSame(TreeNode left, TreeNode right)
    {
        if (left == null && right == null)
        {
            return true;
        }
        else if (left == null || right == null)
        {
            return false;
        }

        return (left.val == right.val && sameSame(left.left, right.right) && sameSame(left.right, right.left));
    }
}