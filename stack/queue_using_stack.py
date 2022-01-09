def enQueue(enqueue_stack, dequeue_stack, key):
    if not enqueue_stack:
        while dequeue_stack:
            enqueue_stack.append(dequeue_stack.pop())
    enqueue_stack.append(key)

def deQueue(enqueue_stack, dequeue_stack):
    if not dequeue_stack:
        while enqueue_stack:
            dequeue_stack.append(enqueue_stack.pop())
    dequeue_stack.pop()

def traverseQueue(enqueue_stack, dequeue_stack):
    if enqueue_stack:
        print(enqueue_stack)
    else:
        print(dequeue_stack[::-1])

if __name__ == '__main__':
    enqueue_stack = []
    dequeue_stack = []

    enQueue(enqueue_stack, dequeue_stack, 5)
    enQueue(enqueue_stack, dequeue_stack, 4)
    enQueue(enqueue_stack, dequeue_stack, 6)
    enQueue(enqueue_stack, dequeue_stack, 2)
    enQueue(enqueue_stack, dequeue_stack, 3)
    traverseQueue(enqueue_stack, dequeue_stack)
    deQueue(enqueue_stack, dequeue_stack)
    traverseQueue(enqueue_stack, dequeue_stack)


