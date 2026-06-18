def find_max(node):
    if node is None:
        return -float('inf')

    return max(node.value, find_max(node.left),find_max(node.right))

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = Node(
    1,
    Node(
        3,
        Node(8,
             Node(14), Node(15)),
        Node(10, Node(3))
    ),
    Node(
        5,
        Node(2),
        Node(6,
             Node(0), Node(1))
    )
)

print(find_max(root))  # 10