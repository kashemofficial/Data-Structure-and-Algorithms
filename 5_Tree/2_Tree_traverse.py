#Tree implement by python 3.
#Time for pre-order() function is O(n).
#Time for in-order() function is O(n).
#Time for post-order() function is O(n).

class Tree_Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self

'''          2             ___ label=0
           /   \ 
          7     9          ___ label=1
         / \      \
        1   6      8       ___ label=2
            / \    / \  
            5  10  3  4    ___ label=3

'''

def create_tree():
    two = Tree_Node(2)
    seven = Tree_Node(7)
    nine = Tree_Node(9)
    two.add_left(seven)
    two.add_right(nine)
    one = Tree_Node(1)
    six = Tree_Node(6)
    seven.add_left(one)
    seven.add_right(six)
    five = Tree_Node(5)
    ten = Tree_Node(10)
    six.add_left(five)
    six.add_right(ten)
    eight = Tree_Node(8)
    nine.add_right(eight)
    three = Tree_Node(3)
    four = Tree_Node(4)
    eight.add_left(three)
    eight.add_right(four)

    return two  #return root node


#Tree traverse to pre-order.
def pre_order(node):
    print(node)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

#Tree traverse to post-order.
def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    print(node)

#Tree traverse to in_order.
def in_order(node):
    if node.left:
        in_order(node.left)
    print(node)
    if node.right:
        in_order(node.right)

if __name__ == '__main__':
    root = create_tree()
    print('____________pre_order____________')
    pre_order(root)
    print('___________post_order____________')
    post_order(root)
    print('____________in_order_____________')
    in_order(root)






