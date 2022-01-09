class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root: Node):
    output_list = []
    if root is None:
        return []
    output_list.extend(inorder_traversal(root.left))
    output_list.append(root.data)
    output_list.extend(inorder_traversal(root.right))
    return output_list

def preorder_traversal(root: Node):
    output_list = []
    if root is None:
        return []
    output_list.append(root.data)
    output_list.extend(preorder_traversal(root.left))
    output_list.extend(preorder_traversal(root.right))
    return output_list

def postorder_traversal(root: Node):
    output_list = []
    if root is None:
        return []
    output_list.extend(postorder_traversal(root.left))
    output_list.extend(postorder_traversal(root.right))
    output_list.append(root.data)
    return output_list

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(3)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(11)
    root.right.left = Node(13)
    root.right.right = Node(15)
    print("Inorder: ", inorder_traversal(root))
    print("PreOrder: ", preorder_traversal(root))
    print("PostOrder", postorder_traversal(root))
    