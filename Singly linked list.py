class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self):
        return self.size

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        self.size += 1

    def add_middle(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")

        if index == 0:
            self.add_first(data)
            return

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            raise IndexError("List is empty")

        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def remove_last(self):
        if self.head is None:
            raise IndexError("List is empty")

        if self.head.next is None:
            return self.remove_first()

        temp = self.head
        while temp.next.next:
            temp = temp.next

        data = temp.next.data
        temp.next = None
        self.size -= 1
        return data

    def remove_middle(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")

        if index == 0:
            return self.remove_first()

        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        data = temp
