class Node(object):
    def __init__(self, key):
        self.data = key
        self.nect = None

class CircukarLinkedlist:
    def __init__(self):
        self.head = None
    
    def insertAtEnd(self, key):
        node = Node(key)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node 
        node.next = self.head
    
    def traverse(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()


if __name__ == '__main__':
    ll = CircukarLinkedlist()
    ll.insertAtEnd(1)
    ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.insertAtEnd(4)
    ll.traverse()