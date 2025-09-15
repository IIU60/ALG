class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

one = TreeNode(value=1)
two = TreeNode(value=2)
three = TreeNode(value=3)
four = TreeNode(value=4)
five = TreeNode(value=5)

one.left, one.right = two, three
two.left, two.right = four, five
