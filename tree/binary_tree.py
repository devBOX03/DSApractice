from queue import Queue
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

def insertNode(root: Node, key):
    if root is None:
        return
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        current: Node = queue.queue[0]
        queue.get()

        if current.left is None:
            current.left = Node(key)
            break
        else:
            queue.put(current.left)
        if current.right is None:
            current.right = Node(key)
            break
        else:
            queue.put(current.right)

def removeNode(root, key):
    if root is None:
        return -1
    queue = Queue()
    queue.put(root)
    key_node = None
    current = None
    last_parent_ptr_left = None
    last_parent_ptr_right = None
    while not queue.empty():
        current: Node = queue.queue[0]
        queue.get()
        if current.data == key:
            key_node = current
        if current.left is not None:
            last_parent_ptr_left = current
            queue.put(current.left)
        if current.right is not None:
            last_parent_ptr_right = current
            queue.put(current.right)
    if key_node:
        key_node.data = current.data
        if last_parent_ptr_left.left == current:
            last_parent_ptr_left.left = None
        if last_parent_ptr_right.right == current:
            last_parent_ptr_right.right = None
        return root
    return -1


if __name__ == '__main__':
    root = Node(1)
    insertNode(root, 3)
    insertNode(root, 5)
    insertNode(root, 7)
    insertNode(root, 11)
    insertNode(root, 13)
    insertNode(root, 15)
    result = removeNode(root, 3)
    print("Found" if result != -1 else "Not Found")
    print("Inorder: ", inorder_traversal(root))
    print("PreOrder: ", preorder_traversal(root))
    print("PostOrder", postorder_traversal(root))
    