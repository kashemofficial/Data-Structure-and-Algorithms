'''class selection_sort:
    def __init__(self,L):
        self.L = L
        n = len(L)
        for i in range(0,n-1):
            index_min = i
            for j in range(i+1,n):
                if L[j] < L[index_min]:
                    index_min = j
            L[i],L[index_min] = L[index_min],L[i]
        print(L)
if __name__ == '__main__':
    L = [5,3,2,1,4]
    selection_sort(L)'''

'''def selection_sort(L):
    n = len(L)
    for i in range(0,n-1):
        index_min = i
        for j in range(i+1,n):
            if L[j] < L[index_min]:
                index_min = j
        L[i],L[index_min] = L[index_min],L[i]
    print(L)

if __name__ == '__main__':
    L = [5,3,1,2,4]
    selection_sort(L)
'''

L = [5,3,1,2,4]
n = len(L)
for i in range(0,n-1):
    index_min = i
    for j in range(i+1,n):
        if L[j] < L[index_min]:
            index_min = j
    L[i],L[index_min] = L[index_min],L[i]
print(L)







