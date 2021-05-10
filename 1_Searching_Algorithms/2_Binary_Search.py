''' Time Complexity     : O(log n)
    Space Complexity    : O(1)
'''

class binary_search:
    def __init__(self,L,item):
        self.L = L
        self.item = item
        left = 0
        right = len(L)-1
        while left <= right:
            mid = (left + right)//2
            if L[mid] == item:
                print(mid)
                break
            elif L[mid] < item:
                left = mid + 1
            else:
                right = mid - 1
        else:
            print('Sorry this is wrong')

if __name__ == '__main__':
    L = [1,2,3,4,5,6,7]
    item = int(input())
    binary_search(L,item)




