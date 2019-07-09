class node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def to_string(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def get(self):
        current_node = self.head
        list = []
        while current_node.next != 0:
            list.append(current_node.data)
        print(list)

    def pr(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def length(self):
        count = 0
        curr = self.head
        while curr:
            count = count + 1
            curr = curr.next
        return count

    def deletelastnode(self):
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None

    def deletefirstnode(self):
        curr = self.head
        self.head = curr.next

