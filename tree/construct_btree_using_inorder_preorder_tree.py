class Node:
    def __init__(self, element):
        self.data = element
        self.left = None
        self.right = None

def buildTree(inoOrder: list, preOrder: list, inStart: int, inEnd: int, preStart: int) -> Node:
    if inStart > inEnd:
        return
    
    rootVal = preOrder[preStart]
    rootIndex = inoOrder.index(rootVal)
    treeNode: Node = Node(rootVal)

    if inStart == inEnd:
        return treeNode

    leftPreOrderStart = preStart + 1
    rightPreOrderStart = preStart + (rootIndex - inStart) + 1
    treeNode.left = buildTree(inoOrder, preOrder, inStart, rootIndex-1, leftPreOrderStart)
    treeNode.right = buildTree(inoOrder, preOrder, rootIndex+1, inEnd, rightPreOrderStart)

    return treeNode

def inorderTraverse(root: Node):
    output_tree_list = []
    if root is None:
        return output_tree_list

    output_tree_list.extend(inorderTraverse(root.left))

    output_tree_list.append(root.data)
    output_tree_list.extend(inorderTraverse(root.right))

    return output_tree_list

if __name__ == '__main__':
    inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
    preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
    tree = buildTree(inOrder, preOrder, 0, len(inOrder)-1, 0)
    print(tree)
    if tree:
        print(inorderTraverse(tree))
    else:
        print("Empty tree")

