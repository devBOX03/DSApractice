def getParent(index):
    return (index-1) // 2

def heapifyMinHeap(arr, size, index):
    smallest = index
    left = 2*index + 1
    right = 2*index + 2
    if left < size and arr[smallest] > arr[left]:
        smallest = left
    if right < size and arr[smallest] > arr[right]:
        smallest = right
    if smallest != index:
        arr[smallest], arr[index] = arr[index], arr[smallest]
        heapifyMinHeap(arr, size, smallest)

def buildMinHeap(arr):
    if not arr:
        return
    arr_length = len(arr)
    if arr_length <= 1:
        return
    start_index = getParent(arr_length-1)
    for index in range(start_index, -1, -1):
        heapifyMinHeap(arr, arr_length, index)

def insert(arr, key):
    arr.append(key)
    arr_length = len(arr)
    if arr_length == 1:
        return
    parent_index = getParent(arr_length - 1)
    start_index = arr_length - 1
    while parent_index > -1 and arr[parent_index] > arr[start_index]:
        arr[parent_index], arr[start_index] = arr[start_index], arr[parent_index]
        parent_index, start_index = getParent(parent_index), parent_index


def deleteAtIndex(arr, index):
    if not arr:
        return -1
    arr_length = len(arr)
    if arr_length <= index:
        return -1
    parent_index = getParent(index)
    arr[index] = float('-inf')
    while parent_index > -1 and arr[parent_index] > arr[index]:
        arr[parent_index], arr[index] = arr[index], arr[parent_index]
        parent_index, index = getParent(parent_index), parent_index
    extractMin(arr)

def extractMin(arr):
    if not arr:
        return
    start_index = 0
    arr[start_index] = arr.pop()
    arr_length = len(arr)
    if arr_length <= 1:
        return
    heapifyMinHeap(arr, arr_length, start_index)

def kth_minimum(arr, k):
    if not arr:
        return -1
    if len(arr) <= k:
        return -1
    # build min heap
    buildMinHeap(arr)
    index = 0
    while index < k-1:
        extractMin(arr)
        index += 1
    return arr[0]


if __name__ == '__main__':
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    arr.reverse()
    buildMinHeap(arr)
    print("Heap %s" % arr)
    insert(arr, 0)
    print("After insertion of element %s" % arr)
    extractMin(arr)
    print("After extraction of top element %s" % arr)
    deleteAtIndex(arr, 2)
    print("Array after deletion %s" % arr)
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    print("Kth minimum :=> %s" % kth_minimum(arr, 3))

# Final Heap:
#             1
#           /    \
#          3       6
#        /  \     / \
#       4    10  13  8
#      / \   / \
#     9   5 15  17

