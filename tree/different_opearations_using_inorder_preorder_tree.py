class Node:
    def __init__(self, element):
        self.data = element
        self.left = None
        self.right = None

def searchIndex(array, key):
    for index in range(len(array)):
        if array[index] == key:
            return index
    return -1

def buildTree(in_arr, pre_arr, in_start_index, in_end_index, pre_start_index):
    '''
    Build tree from inorder and preorder array
    '''
    if in_start_index > in_end_index:
        return

    root_value = pre_arr[pre_start_index]
    root_index = searchIndex(in_arr, root_value)
    root = Node(root_value)

    if in_start_index == in_end_index:
        return root

    # build left sub tree
    # right sub tree start pre order index
    left_sub_tree_root_pre_order_index = pre_start_index + 1
    root.left = buildTree(in_arr, pre_arr, in_start_index, root_index-1, left_sub_tree_root_pre_order_index)
    # build right sub tree
    # right sub tree start pre order index
    right_sub_tree_root_pre_order_index = pre_start_index + (root_index-in_start_index) + 1
    root.right = buildTree(in_arr, pre_arr, root_index+1, in_end_index, right_sub_tree_root_pre_order_index)

    return root

def inOrderTraversal(root):
    output = []
    if not root:
        return output
    output.extend(inOrderTraversal(root.left))
    output.append(root.data)
    output.extend(inOrderTraversal(root.right))

    return output

def postorderFromInorderPreorder(in_arr, pre_arr, in_start_index, in_end_index, pre_start_index):
    '''
    post order traversal from inorder and preorder
    '''
    output = []
    if in_start_index > in_end_index:
        return output

    root_value = pre_arr[pre_start_index]
    root_index = searchIndex(in_arr, root_value)
    if in_start_index == in_end_index:
        output.append(root_value)
        return output

    # get left subtree
    left_subtree_root_pre_start_index = pre_start_index + 1
    output.extend(postorderFromInorderPreorder(in_arr, pre_arr, in_start_index, root_index-1, left_subtree_root_pre_start_index))
    # get right subtree
    right_subtree_root_pre_start_index = pre_start_index + (root_index - in_start_index) + 1
    output.extend(postorderFromInorderPreorder(in_arr, pre_arr, root_index+1, in_end_index, right_subtree_root_pre_start_index))
    output.append(root_value)

    return output

if __name__ == '__main__':
    in_order_arr = ['D', 'B', 'E', 'A', 'F', 'C']
    pre_order_arr = ['A', 'B', 'D', 'E', 'C', 'F']
    tree = buildTree(in_order_arr, pre_order_arr, 0, len(in_order_arr)-1, 0)
    post_order_arr = postorderFromInorderPreorder(in_order_arr, pre_order_arr, 0, len(in_order_arr)-1, 0)
    print("Post order: %s" % post_order_arr)
    if tree:
        print(inOrderTraversal(tree))
    else:
        print("Empty tree")
