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
    
    def trverse(self):
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


if __name__ == '__main__':
    ll = LinkedList()
    ll.insertNodeAtEnd(5)
    ll.insertNodeAtEnd(2)
    ll.insertNodeAtEnd(4)
    ll.insertNodeAtEnd(1)
    ll.trverse()
    print(ll.length(ll.head))
    ll.insertNodeAtStart(6)
    ll.trverse()
    print(ll.search(ll.head, 5))
    print(ll.getNthNodeFromEnd(8))
