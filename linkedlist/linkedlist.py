class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    
    def insertNodeAtEnd(self, key):
        node = Node(key)
        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = node
        return node
    
    def insertNodeAtStart(self, key):
        node = Node(key)
        node.next = self.head
        self.head = node
    
    def insertNodeAtPosition(self, key, pos):
        node = Node(key)
        if self.head is None:
            self.head = node
            return

        index = 0
        temp = self.head
        while temp != None:
            index += 1
            if index == pos-1:
                break
            temp = temp.next
        node.next = temp.next
        temp.next = node
    
    def deleteNodeFromStart(self):
        if self.head is None:
            return
        self.head = self.head.next
    
    def deleteNodeFromPosition(self, pos):
        if self.head is None:
            return
        temp = self.head
        index = 0
        while temp != None:
            index += 1
            if index == pos-1:
                break
            temp = temp.next
        if index < pos-1:
            return -1
        temp.next = temp.next.next
    
    def deleteNodeFromEnd(self):
        if self.head is None:
            return

        current = self.head
        previous_node = None
        while current.next is not None:
            previous_node = current
            current = current.next
        if previous_node:
            previous_node.next = None
    
    def traverse(self):
        if self.head is None:
            return

        temp = self.head
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
    
    def length(self, ll):
        if ll is None:
            return 0
        return self.length(ll.next) + 1
    
    def search(self, ll, key):
        if not ll:
            return False
        if ll.data == key:
            return True
        return self.search(ll.next, key)

    def getNthNodeFromEnd(self, n):
        if self.head is None:
            return -1
            
        slow_ptr = self.head
        fast_ptr = self.head
        fast_ptr_pos = 0

        while fast_ptr != None:
            fast_ptr_pos += 1
            if fast_ptr_pos == n:
                break
            fast_ptr = fast_ptr.next
    
        if fast_ptr_pos < n:
            return -1

        while fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next

        return slow_ptr.data

    def getMidOfLinkedList(self):
        if not self.head:
            return None

        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data
    
    def detectLoopInLinkedList(self):
        if self.head is None:
            return False

        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

            if slow_ptr == fast_ptr:
                return True

        return False
    
    def reverse(self):
        if self.head is None:
            return
        
        current = self.head
        prev_node = None
        while current is not None:
            temp = current.next
            current.next = prev_node
            prev_node = current
            current = temp
        self.head = prev_node
    
    def reverseRecursively(self, head: Node):
        if head is None or head.next is None:
            return head
        
        reversed_ll = self.reverseRecursively(head.next)

        head.next.next = head
        head.next = None

        return reversed_ll

    @classmethod
    def getIntersectionPoint(cls, head1: Node, head2: Node):
        if head1 is None or head2 is None:
            return None

        ptr1 = head1
        ptr2 = head2

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr1 == ptr2:
                return ptr1
            if ptr1 is None:
                ptr1 = head2
            if ptr2 is None:
                ptr2 = head1

        return None

if __name__ == '__main__':
    ll = LinkedList()
    ll.insertNodeAtEnd(5)
    ll.insertNodeAtEnd(2)
    ll.insertNodeAtEnd(4)
    ll.insertNodeAtEnd(1)
    ll.traverse()
    ll.deleteNodeFromEnd()
    ll.traverse()
    ll.insertNodeAtEnd(1)
    print("Lenght if linked list %s" % ll.length(ll.head))
    ll.insertNodeAtStart(6)
    ll.traverse()
    target = 5
    print("Target %s found in linked list: %s" % (target, ll.search(ll.head, target)))
    print("%sth node from end: %s" %(8, ll.getNthNodeFromEnd(8)))
    print("Mid element of linked list: %s" % ll.getMidOfLinkedList())
    # reverse linked list
    print("Reverse linked list:---")
    ll.reverse()
    ll.traverse()
    print("Re-reverse linked list:---")
    ll.head = ll.reverseRecursively(ll.head)
    ll.traverse()

    # create two linked lists to make inverted Y shaped linked list
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    head2 = Node(4)
    head2.next = Node(5)
    head2.next.next = Node(6)
    head2.next.next.next = head1.next.next

    result = LinkedList.getIntersectionPoint(head1, head2)
    print("Intersection point present: %s" % (True if result else False))
    
    # create a new linked list for loop
    ll2 = LinkedList()
    ll2.insertNodeAtEnd(5)
    ll2.insertNodeAtEnd(2)
    ll2.insertNodeAtEnd(4)
    ll2.insertNodeAtEnd(1)
    ll2.traverse()
    # check loop
    print("Loop exists: %s" % ll.detectLoopInLinkedList())
    last_node = ll2.insertNodeAtEnd(12)
    last_node.next = ll2.head
    # check loop again
    print("Loop exists: %s" % ll2.detectLoopInLinkedList())

