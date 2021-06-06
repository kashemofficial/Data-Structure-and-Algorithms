class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Prepend(self,New_Data):
        node = Node(New_Data)
        node.next = self.head
        self.head = node

    def Append(self,New_Data):
        node = Node(New_Data)
        if self.head is None:
            self.head = node
            return
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = node

    def Insert(self,Prve,New_Data):
        node = Node(New_Data)
        if Prve == None:
            print('No')
            return
        node.next = Prve.next
        Prve.next = node

    def Print(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next

    def Search(self,item):
        current_Node = self.head

        if current_Node is None:
            return False
        else:
            while current_Node is not None:
                if current_Node.data == item:
                    print(current_Node.data)
                current_Node = current_Node.next


if __name__ == '__main__':
    l = Linked_List()
    l.Prepend(1)
    l.Prepend(2)
    l.Prepend(3)
    l.Prepend(4)
    l.Append('kashem')
    l.Insert(l.head,'bbpi')
    l.Print()
    print()
    l.Search('bbpi')




