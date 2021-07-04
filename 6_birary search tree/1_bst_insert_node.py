'''
        insert() function time complexity   : O(n)
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
        if root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

if __name__ == '__main__':
    root = Node(50)
    '''
          __50__
    '''
    root = insert(root,30)
    '''
            ___ 50 ___
           / 
          30
    '''
    root = insert(root,20)
    '''
                ___ 50 ___
             /
           _30_
         /
        20
    '''
    root = insert(root,40)
    '''
                ___ 50 ___
             /
           _30_
         /      \
        20      40
    '''

    root = insert(root,70)

    '''
                   ___ 50 ___
                /              \
              _30_             70
            /      \
           20      40
    '''
    root = insert(root,60)
    '''
                   ___ 50 ___
                /              \
              _30_           _ 70_
            /      \       /    
           20      40     60
       '''
    root = insert(root,80)
    '''
                   ___ 50 ___
                /              \
              _30_           _ 70_
            /      \       /       \
           20      40     60       80 
       '''
    inorder(root)





