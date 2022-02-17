def counting_sort(count):
    sort_li = []
    for index,value in enumerate(count):
        if value > 0:
            sort_li.extend([index]*value)
    print(sort_li)
if __name__ == '__main__':
    count = list(map(int,input().split()))
    counting_sort(count)