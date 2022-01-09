from queue import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getTreeHeight(root: None) -> int:
    if root is None:
        return 0

    leftTreeHeight = getTreeHeight(root.left) + 1
    rightTreeHeight = getTreeHeight(root.right) + 1

    return leftTreeHeight if leftTreeHeight > rightTreeHeight else rightTreeHeight

def levelOrderTraversalBruteForce(root: None) -> None:
    if root is None:
        print("Trees is empty")
    
    treeHeight = getTreeHeight(root)
    treeAsList = []
    for level in  range(1, treeHeight+1):
        treeAsList.extend(printCurrentLevel(root, level))
    
    print(treeAsList)


def printCurrentLevel(root: Node, level: int) -> list:
    output = []
    firstLevel = 1
    secondLevel = 2
    prevLevel = level - 1

    if root is None:
        return output

    if level == firstLevel:
        output.append(root.data)
    elif level >= secondLevel:
        output.extend(printCurrentLevel(root.left, prevLevel))
        output.extend(printCurrentLevel(root.right, prevLevel))

    return output

def levelOrderTraversal(root: Node):
    node_queue = []
    current_node: Node = None
    queueFront = 0
    if root is None:
        return
    node_queue.append(root)
    while node_queue:
        print(node_queue[queueFront].data, end=" ")
        current_node = node_queue.pop(queueFront)

        if current_node.left is not None:
            node_queue.append(current_node.left)
        if current_node.right is not None:
            node_queue.append(current_node.right)

def levelOrderTraversalByLevel(root: Node):
    queueFront = 0
    final_tree_node_by_level = []
    node_queue = []
    if root is None:
        return final_tree_node_by_level
    
    temp_node_by_level = []
    current_node = None
    node_queue = [root, None]
    while node_queue:
        if node_queue[queueFront] is None:
            if len(node_queue) >=2:
                node_queue.append(node_queue.pop(queueFront))
            else:
                node_queue.pop(queueFront)
            final_tree_node_by_level.append(temp_node_by_level)
            temp_node_by_level = []
            continue
        temp_node_by_level.append(node_queue[queueFront].data)
        current_node = node_queue.pop(queueFront)
        if current_node.left is not None:
            node_queue.append(current_node.left)
        if current_node.right is not None:
            node_queue.append(current_node.right)
    print(final_tree_node_by_level)

# Vertical order traversal
## Bruteforce starts from here
def findMinMaxDistance(root: Node, minimun: list, maximum: list, distance: int):
    if root is None:
        return
    minimun[0] = distance if distance < minimun[0] else minimun[0]
    maximum[0] = distance if distance > maximum[0] else maximum[0]

    findMinMaxDistance(root.left, minimun, maximum, distance-1)
    findMinMaxDistance(root.right, minimun, maximum, distance+1)

def getVerticalOrderedItems(root: Node, distance: int, target_distance: int):
    output = []
    if root is None:
        return output

    if distance == target_distance:
        output.append(root.data)

    output.extend(getVerticalOrderedItems(root.left, distance-1, target_distance))
    output.extend(getVerticalOrderedItems(root.right, distance+1, target_distance))

    return output

def verticalOrderTraversalBruteForce(root: Node):
    output = []
    minimum = [0]
    maximum = [0]
    horizonatalDistance = 0

    findMinMaxDistance(root, minimum, maximum, horizonatalDistance)
    for distance in range(minimum[0], maximum[0]+1):
        output.append(getVerticalOrderedItems(root, 0, distance))

    print(output)

## BruteForce ends here

## Optimized vertical ordered traversal
def storeNodesByDistance(root: Node, distanceNodeDict: dict, minimum: list,
                         maximum: list, distance: int):
    if root is None:
        return
    minimum[0] = distance if distance < minimum[0] else minimum[0]
    maximum[0] = distance if distance > maximum[0] else maximum[0]
    if distance in distanceNodeDict:
        distanceNodeDict[distance].append(root.data)
    else:
        distanceNodeDict[distance] = [root.data]
    
    storeNodesByDistance(root.left, distanceNodeDict, minimum, maximum, distance-1)
    storeNodesByDistance(root.right, distanceNodeDict, minimum, maximum, distance+1)


def verticalOrderedTraversal(root: Node) -> None:
    output = []
    minimum = [0]
    maximum = [0]
    startRootDistance = 0
    distanceNodeDict: dict[list] = dict()

    storeNodesByDistance(root, distanceNodeDict, minimum, maximum, startRootDistance)
    for distance in range(minimum[0], maximum[0]+1):
        if distance in distanceNodeDict:
            output.append(distanceNodeDict[distance])
    
    print(output)

## optimized vertical ordered ends here

# Top ordered view
def storeNodesByDistanceTopView(root: Node, distanceNodeDict: dict,
                                minimum: list, distance: int, level: int):
    if root is None:
        return

    minimum[0] = distance if distance < minimum[0] else minimum[0]
    if distance not in distanceNodeDict:
        distanceNodeDict[distance] = [root.data, level]
    elif distanceNodeDict[distance][1] > level:
        distanceNodeDict[distance] = [root.data, level]
    
    storeNodesByDistanceTopView(root.left, distanceNodeDict, minimum, distance-1, level+1)
    storeNodesByDistanceTopView(root.right, distanceNodeDict, minimum, distance+1, level+1)

def topOrderedTraversal(root: Node) -> None:
    output = []
    minimum = [0]
    startRootDistance = 0
    depth = 1
    distanceNodeDict: dict[list] = dict()

    storeNodesByDistanceTopView(root, distanceNodeDict, minimum, startRootDistance, depth)
    index = minimum[0]
    while index in distanceNodeDict:
        output.append(distanceNodeDict[index][0])
        index += 1
    
    print(output)

def topOrderedViewOptimized(root: Node):
    if root is Node:
        return
    output = []
    nodeQueue: deque = deque([(root, 0)])
    distanceNodeDict = dict()
    minimumDistance = float('inf')

    while nodeQueue:
        current = nodeQueue.popleft()

        if current[1] not in distanceNodeDict:
            distanceNodeDict[current[1]] = current[0].data
            minimumDistance = minimumDistance if minimumDistance < current[1] else current[1]
        if current[0].left:
            nodeQueue.append([current[0].left, current[1]-1])
        if current[0].right:
            nodeQueue.append([current[0].right, current[1]+1])
    while minimumDistance in distanceNodeDict:
        output.append(distanceNodeDict[minimumDistance])
        minimumDistance += 1
    print(output)

# top view ends here

# right view starts from here
def rightView(root: Node):
    if root is None:
        return
    output = []
    nodeQueue: deque = deque([(root, 0)])
    firstIndex = 0
    secondQueueIndex = 1
    distanceNodeDict = dict()
    maxDepth = -1

    while nodeQueue:
        currentQueueElement = nodeQueue.popleft()

        if currentQueueElement[secondQueueIndex] not in distanceNodeDict:
            maxDepth += 1
        distanceNodeDict[currentQueueElement[secondQueueIndex]] = currentQueueElement[firstIndex].data
        if currentQueueElement[firstIndex].left:
            nodeQueue.append([currentQueueElement[firstIndex].left, currentQueueElement[secondQueueIndex]+1])
        if currentQueueElement[firstIndex].right:
            nodeQueue.append([currentQueueElement[firstIndex].right, currentQueueElement[secondQueueIndex]+1])

    for index in range(maxDepth+1):
        output.append(distanceNodeDict[index])
    print(output)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # levelOrderTraversalBruteForce(root)
    # levelOrderTraversal(root)
    # levelOrderTraversalByLevel(root)
    verticalOrderTraversalBruteForce(root)
    verticalOrderedTraversal(root)
    topOrderedTraversal(root)
    topOrderedViewOptimized(root)
    rightView(root)
    pass