#ki vabe data add hoy node a
'''class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

head = Node(5)
print(head.val)

head.next = Node(10)
print(head.next.val)

head.next.next = Node(15)
print(head.next.next.val)'''


class Node:

    # data, next
    def __init__(self, data):
        self.val = data
        self.next = None

class linkedlist:

    def __init__(self):
        self.head = None

    def Append(self, new_data):
                              # 10
        current_value = Node(new_data)

        if self.head is None:
            self.head = current_value # 10
            return

        count = self.head

        while count.next is not None:

            count = count.next

        count.next = current_value

    def print_linked_list(self):
        temp = self.head

        while temp is not None:
            print(temp.val, end=" ")

            temp = temp.next

if __name__ == '__main__':
    l = linkedlist()
    l.Append(5)
    l.Append(10)
    l.Append(20)
    l.Append(12)
    l.print_linked_list()


