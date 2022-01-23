def reverseStack(stack: list):
    if not stack:
        return
    top_element = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top_element)

def insertAtBottom(stack: list, item):
    if not stack:
        stack.append(item)
    else:
        top_element = stack.pop()
        insertAtBottom(stack, item)
        stack.append(top_element)

if __name__ == '__main__':
    stack = list()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    reverseStack(stack)
    print(stack)

