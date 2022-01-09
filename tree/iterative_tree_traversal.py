
class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def inorder_traversal(root: Node):
    output_list: int = []
    node_stack: Node = []
    current_node: Node = root
    if root is None:
        return []
    while node_stack or current_node:
        if current_node is not None:
            node_stack.append(current_node)
            current_node = current_node.left
        else:
            current_node = node_stack.pop()
            output_list.append(current_node.key)
            current_node = current_node.right

    return output_list

def preorder_traversal(root: Node):
    output_list: int = []
    node_stack: Node = []
    current_node: Node = root
    if root is None:
        return []
    while node_stack or current_node:
        if current_node is not None:
            output_list.append(current_node.key)
            node_stack.append(current_node)
            current_node = current_node.left
        else:
            current_node = node_stack.pop()
            current_node = current_node.right

    return output_list

def postorder_traversal(root: Node):
    output_list: int = []
    node_stack: Node = []
    current_node: Node = root
    if root is None:
        return []
    while node_stack or current_node:
        if current_node is not None:
            node_stack.append(current_node)
            node_stack.append(current_node)
            current_node = current_node.left
        else:
            current_node = node_stack.pop()
            if current_node == peek(node_stack):
                current_node = current_node.right
            else:
                output_list.append(current_node.key)
                current_node = None

    return output_list

def peek(stack: Node):
    if len(stack) < 1:
        return None
    return stack[-1]

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