def getParent(index):
    return (index-1) // 2

def heapify(arr, size, index):
    largest = index
    left = 2*index + 1
    right = 2*index + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    
    if right < size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]

        # check heapify for below nodes
        heapify(arr, size, largest)

def insert(arr, element):
    arr.append(element)
    arr_size = len(arr)
    start_index = (arr_size-1) // 2
    index = arr_size - 1

    while start_index > -1 and arr[start_index] < arr[index]:
        arr[start_index], arr[index] = arr[index], arr[start_index]
        start_index, index = (start_index-1) // 2, start_index

def extractMax(arr):
    arr[0] = arr.pop()
    heapify(arr, len(arr), 0)

def deleteAtIndex(arr, index):
    if not arr:
        return -1
    if len(arr) <= index:
        return -1
    arr[index] = float('inf')
    parent = getParent(index)
    # move element to the top as it is the latest element
    while parent > -1 and arr[parent] < arr[index]:
        arr[parent], arr[index] = arr[index], arr[parent]
        parent, index = getParent(parent), parent
    # remove the top element
    extractMax(arr)

def buildMaxHeap(arr):
    arr_length = len(arr)
    start_index = (arr_length-1)//2
    for index in range(start_index, -1, -1):
        heapify(arr, arr_length, index)

def kth_maximum(arr, k):
    if not arr:
        return -1
    if len(arr) <= k:
        return -1
    # build min heap
    buildMaxHeap(arr)
    index = 0
    while index < k-1:
        extractMax(arr)
        index += 1
    return arr[0]

if __name__ == '__main__':
    # arr = [1,2,3,4,5,6,7,8]
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    buildMaxHeap(arr)
    print("Heap %s" % arr)
    insert(arr, 19)
    print("After insertion of element %s" % arr)
    extractMax(arr)
    print("After extraction of top element %s" % arr)
    deleteAtIndex(arr, 2)
    print("Array after deletion %s" % arr)
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    print("Kth minimum :=> %s" % kth_maximum(arr, 3))

# Final Heap:
#             17
#           /    \
#         15      13
#        /  \     / \
#       9     6  5   10
#      / \   / \
#     4   8 3   1
