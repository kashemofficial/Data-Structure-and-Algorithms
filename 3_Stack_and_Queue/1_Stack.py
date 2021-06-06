"""
    Complicity of push() function:- O(1)
    Complicity of pop() function:- 0(1)
"""
#LIFO
# Stack = Last in First Out

class Stack:
    def __init__(self):
        self.item = []
        self.size = 0

    def Data_Add(self,NewData):
        self.item.append(NewData)
        self.size += 1

    def Out_Element(self):
        self.size -= 1
        return self.item.pop()

    def Print_Stack(self):
        return self.item

    def Is_Empty_Stack(self):
        if self.size == 0:
            return 'Stack is Empty!!'
        else:
            return "Stack is Full"

    def Reverse_Data(self):
        return self.item[::-1]

    def First_Data(self):
        return self.item[0]

    def Last_Data(self):
        return self.item[-1]

if __name__ == '__main__':
    op = Stack()
    op.Data_Add('0. Islam'),op.Data_Add('1. Bangla'),op.Data_Add('2. English'),op.Data_Add('3. Math')
    print("Before Stack",op.Print_Stack())
    print('Before Stack Size',op.size)

    op.Out_Element(),op.Out_Element()
    print('After Stack',op.Print_Stack())
    print('After Stack Size',op.size)

    print("Reverse Stack",op.Reverse_Data())

    print(op.Is_Empty_Stack())

    print("It is Stack first Element", op.First_Data())
    print('It is Stack Last Element',op.Last_Data())
