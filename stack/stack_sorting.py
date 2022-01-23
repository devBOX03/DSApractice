def sortStack(stack):
    if not stack:
        return
    top_element = stack.pop()
    sortStack(stack)
    insertAtCorrrectPos(stack, top_element)

def insertAtCorrrectPos(stack, item):
    if not stack or stack[-1] >= item:
        stack.append(item)
    else:
        top_element = stack.pop()
        insertAtCorrrectPos(stack, item)
        stack.append(top_element)


if __name__ == '__main__':
    stack = list()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    print("Stack: %s" % stack)
    sortStack(stack)
    print("Sorted Stack: %s" % stack)
