class Node:
    def __init__(self,Data):
        self.data = Data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Append(self,New_Data):
        current_data = Node(New_Data)
        if self.head is None:
            self.head = current_data
            return
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = current_data

    def Insert(self,prve,New_Data):
        if prve == None:
            return
        node = Node(New_Data)
        node.next = prve.next
        prve.next = node

    def Print_Linked_List(self):
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
    li.Insert(li.head.next,'kashem')
    li.Print_Linked_List()

