
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def reverse(self, head):

        if head is None or head.next is None:
            return head
        rest = self.reverse(head.next)
        head.next.next = head
        head.next = None

        return rest

    def __str__(self):
        linkedListStr = ""
        temp = self.head
        while temp:
            linkedListStr = (linkedListStr +
                             str(temp.data) + " ")
            temp = temp.next
        return linkedListStr

    def push(self, data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp



liList = LinkedList()
liList.push(20)
liList.push(4)
liList.push(15)
liList.push(85)

print("linked list")
print(liList)

liList.head = liList.reverse(liList.head)

print("Reversed L_List")
print(liList)
