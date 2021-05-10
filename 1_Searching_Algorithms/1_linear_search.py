"""Time Complexity     : O(n)
    Space Complexity    : O(1)"""
class linear_search:
    def __init__(self,L,item):
        self.L = L
        self.item = item
        for i in range(len(L)):
            if L[i] == item:
                print(i)
                break
        else:
            print("Sorry This is Wrong")

if __name__ == '__main__':
    L = [1,2,3,4,5]
    item = int(input())
    linear_search(L,item)

