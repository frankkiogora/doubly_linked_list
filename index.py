class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublLinkedList:
    def __init__(self):
        self.head = None

# append

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node

        else:

            new_node = Node(data)
            cur = self.head

            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

# prepend

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            new_node.next = self.head
            self.head = new_node

        else:

            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

#Add node Before

    def add_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
            cur = cur.next

#Add node after

    def add_after_node(self, key, data):
        cur = self.head 
        while cur:
            if cur.next is None and cur.data == key:
                self.append(data)
            elif cur.data == key:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                nxt.prev = new_node
            cur = cur.next

#Print list

    def print_list(self):
        cur = self.head
        while cur:
            print cur.data
            cur = cur.next



dllist = DoublLinkedList()

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)
dllist.append(6)
dllist.prepend(0)

dllist.add_before_node(4,9)
dllist.print_list()

dllist.add_after_node(3,6)

dllist.print_list()








