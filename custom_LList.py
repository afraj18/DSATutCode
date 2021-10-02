class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def add(self, new):
        new_node = Node(new)
        new_node.next = self.head
        self.head = new_node
    def reverse(self):
        ListNode

link = Linked()
elem = Node("Afraj")
link.head = elem
elem2 = Node("AJ")
link.head.next = elem2
# # elem3 = Node("Appaji")
# # link.head.next = elem3
# elem4 = Node("Afa")
link.add("Appaji")
link.show()
