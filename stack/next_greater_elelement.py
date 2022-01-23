def getNextGreaterElement(array: list) -> None:
    if len(array) <= 0:
        return
    print(bruteForce(array))
    print(optimizationUsingSpace(array))

# bruteforce
def bruteForce(array: list) -> list:
    '''
    time complexicity: O(n^2)
    space complexicity: O(1)
    '''
    greater_element_list = [-1] * len(array)

    for index, element in enumerate(array):
        for next_element in array[index+1:]:
            if next_element > element:
                greater_element_list[index] = next_element
                break

    return greater_element_list

# optimized using space
def optimizationUsingSpace(array: list) -> list:
    '''
    time complexicity: O(n)
    space complexicity: O(n)
    '''
    greater_element_stack: list = []
    next_greater_element_list: list = [-1] * len(array)
    top = -1

    # iterate array from end
    for index in range(len(array)-1, -1, -1):
        # pop smaller elements
        while greater_element_stack and array[index] >= greater_element_stack[top]:
            greater_element_stack.pop()
        if greater_element_stack:
            next_greater_element_list[index] = greater_element_stack[top]
        greater_element_stack.append(array[index])

    return next_greater_element_list


if __name__ == '__main__':
    arr1 = [4,5,2,25]
    arr2 = [6,8,0,1,3]
    getNextGreaterElement(arr1)
    getNextGreaterElement(arr2)
