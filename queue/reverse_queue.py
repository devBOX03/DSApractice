from queue import Queue

# using space
def reverseQueue(queue: Queue):
    stack: list = []
    while not queue.empty():
        stack.append(queue.queue[0])
        queue.get()
    while stack:
        queue.put(stack[-1])
        stack.pop()

# using recursion
def reverseQueueRecur(queue: Queue):
    if queue.empty():
        return
    temp = queue.queue[0]
    queue.get()
    reverseQueueRecur(queue)
    queue.put(temp)

def printQueue(q: Queue):
    while not q.empty():
        print(q.queue[0], end=' ')
        q.get()
    print()

if __name__ == '__main__':
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    q.put(5)

    # reverseQueue(q)
    reverseQueueRecur(q)
    printQueue(q)