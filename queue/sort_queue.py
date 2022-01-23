from multiprocessing import cpu_count
from queue import Queue

def getQueueMin(queue, sortedIndex):
    min_value = float('inf')
    min_index = None
    for index in range(queue.qsize()):
        current = queue.queue[0]
        queue.get()
        if current < min_value and index < sortedIndex:
            min_value = current
            min_index = index
        queue.put(current)
    
    return min_index

def insertMinAtEnd(queue, min_index):
    min_value = None
    for index in range(queue.qsize()):
        current = queue.queue[0]
        queue.get()
        if index != min_index:
            queue.put(current)
        else:
            min_value = current
    queue.put(min_value)

def sortQueue(queue: Queue):
    if queue.empty():
        return

    for index in range(queue.qsize()):
        min_index = getQueueMin(queue, queue.qsize() - index)
        insertMinAtEnd(queue, min_index)

def printQueue(queue):
    for _ in range(queue.qsize()):
        current = queue.queue[0]
        queue.get()
        print(current, end=' ')
        queue.put(current)
    print()

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(4)
    q.put(2)
    q.put(5)
    q.put(3)

    sortQueue(q)
    printQueue(q)