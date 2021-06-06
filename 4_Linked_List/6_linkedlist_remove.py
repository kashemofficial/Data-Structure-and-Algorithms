class Node:
    def __init__(self,Data):
        self.data = Data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Append(self, New_Data):
        node = Node(New_Data)
        if self.head is None:
            self.head = node
            return
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = node

    def remove(self, position):
        if position == 0:
            self.head = self.head.next
        else:
            node = self.head
            for _ in range(position - 1):
                node = node.next
            node.next = node.next.next
        return self.head

    def Print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next

if __name__ == '__main__':
    li = Linked_List()
    li.Append(1)
    li.Append(2)
    li.Append(3)
    li.Append(4)
    li.Print_list()
    print()
    li.remove(2)
    li.Print_list()

