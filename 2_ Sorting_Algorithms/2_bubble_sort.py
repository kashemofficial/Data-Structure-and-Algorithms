
li = [1,2,3,4,5]
#    0 1 2 3 4
print('before sort = ',li)
n = len(li)
count = 0
#outer loop
for i in range(0,n):
    # inner loop
    s = 0
    for j in range(n - 1 - i):
        count += 1
        if li[j] > li[j+1]:
            # 12   3
            li[j],li[j+1] = li[j+1],li[j]
            s = 1
    if s == 0:
        break

print('after sort = ',li)

print('count = ',count)


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

'''class Bubble_sort:
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
    Bubble_sort(L)'''
