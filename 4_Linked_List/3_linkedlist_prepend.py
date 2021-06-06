class Node:
    def __init__(self,Data):
        self.value = Data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def Append(self,New_Data):
        current_value = Node(New_Data)
        if self.head is None:
            self.head = current_value
            return
        tail = self.head
        while tail.next is not None:
            tail = tail.next
        tail.next = current_value

    def Prepend(self,New__Data):
        node = Node(New__Data)
        node.next = self.head
        self.head = node

    def Print_list(self):
        temp = self.head
        while temp is not  None:
            print(temp.value,end=" ")
            temp = temp.next

if __name__ == '__main__':
    l = Linked_List()
    l.Append(1)
    l.Append(2)
    l.Append(3)
    l.Append(4)
    l.Prepend(0)
    l.Prepend(10)
    l.Print_list()


