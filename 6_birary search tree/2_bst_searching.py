'''
    insert() function time complexity : 0(n)
    search() function time complexity : 0(n)

'''
class Node:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    else:
        if root.val < key :
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

def search(root,item):
    if root is None or root.val == item:
        return root
    if root.val < item:
        return search(root.right,item)
    return search(root.left,item)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

if __name__ == '__main__':
    root = Node(50)
    root = insert(root,30)
    root = insert(root,20)
    root = insert(root,40)
    root = insert(root,70)
    root = insert(root,60)
    inorder(root)
    print('_________===_______===_______')
    if search(root,50):
        print('Yes')
    else:
        print('No')
