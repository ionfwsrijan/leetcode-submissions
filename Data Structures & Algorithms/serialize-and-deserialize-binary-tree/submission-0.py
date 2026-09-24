class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if root is None:
            return ''
        res = []

        def preorder(root):
            if root is None:
                res.append("#,")
                return
            res.append(str(root.val) + ",")
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ''.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(',')

        def inner():
            first = vals.pop(0)
            if first == '#':
                return None
            return TreeNode(int(first), inner(), inner()) 
            # seems using a constructor __init__(val, left, right)

        return inner()