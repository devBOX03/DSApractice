class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(root: Node, key) -> Node:
    if root is None:
        return Node(key)
    
    if root.data == key:
        return root
    elif key > root.data:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)

    return root

def delete(root: Node, target: int):
    if root is None:
        return None
    if root.data > target:
        root.left = delete(root.left, target)
    elif root.data < target:
        root.right = delete(root.right, target)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        if root.right is None:
            temp = root.left
            root = None
            return temp
        smallestNode = minNode(root.right)
        root.data = smallestNode.data
        root.right = delete(root.right, smallestNode.data)

    return root

def minNode(root: Node):
    if root is None:
        return None
    currentNode: Node = root
    while currentNode.left is not None:
        currentNode = currentNode.left
    return currentNode

def isBST(root: Node, l: Node=None, r: Node=None):
    if root is None:
        return True
    if l is not None and root.data <= l.data:
        return False
    if r is not None and root.data >= r.data:
        return False
    return isBST(root.left, l, root) and isBST(root.right, root, r)

def inorderTraversal(root: Node) -> list:
    output = []
    if root is None:
        return output

    output.extend(inorderTraversal(root.left))
    output.append(root.data)
    output.extend(inorderTraversal(root.right))

    return output

if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 10)
    insert(root, 20)
    insert(root, 70)
    insert(root, 80)
    insert(root, 30)
    insert(root, 40)
    insert(root, 60)
    print(inorderTraversal(root))

    root = delete(root, 30)
    print(inorderTraversal(root))

    # check balanced search tree
    print(isBST(root))
    root.left.left = Node(30)
    print(inorderTraversal(root))
    print(isBST(root))
