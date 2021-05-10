'''L = [5,3,1,4,2]
n = len(L)
for i in range(0,n):
    for j in range(n-i-1):
        if L[j] > L[j+1]:
            L[j],L[j+1] = L[j+1],L[j]
print(L)
'''
'''def bubble_sort(L):
    n = len(L)
    for i in range(0,n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    print(L)
if __name__ == '__main__':
    L = [3,1,7,6,2]
    bubble_sort(L)
'''
class Bubble_sort:
    def __init__(self,L):
        self.L = L
        n = len(L)
        for i in range(0,n):
            for j in range(n-i-1):
                if L[j] > L[j+1]:
                    L[j],L[j+1] = L[j+1],L[j]
        print(L)
if __name__ == '__main__':
    L = [3,2,10,8,9,7,5,6,4,1]
    Bubble_sort(L)




