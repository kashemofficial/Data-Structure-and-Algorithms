class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self,node):
        self.left = node

    def add_right(self,node):
        self.right = node

'''          2             ___ label=0
           /   \ 
          7     9          ___ label=1
         / \      \
        1   6      8       ___ label=2
            / \    / \  
            5  10  3  4    ___ label=3

'''

def create_tree():
    two = Node(2)
    seven = Node(7)
    nine = Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Node(1)
    six = Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Node(5)
    ten = Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Node(8)
    nine.add_right(eight)
    three = Node(3)
    four = Node(4)
    eight.add_left(three)
    eight.add_right(four)

    print('root :',two)
    print('Two left :',seven)
    print('Seven left :',one)
    print('Seven right :',six)
    print('six left :',five)
    print('six right :',ten)
    print('Two right :',nine)
    print('Nine right :',eight)
    print('Eight left :',three)
    print('Eight right :',four)

if __name__ == '__main__':
    create_tree()

