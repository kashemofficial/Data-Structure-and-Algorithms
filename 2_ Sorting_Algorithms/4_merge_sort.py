def Merge_Sort(li):
    size = len(li)
    if size>1:
        mid = size//2
        left_arr = li[:mid]
        l_size = len(left_arr)

        right_arr = li[mid:]
        r_size = len(right_arr)

        #Sorting left_arr
        Merge_Sort(left_arr)
        #Sorting right_arr
        Merge_Sort(right_arr)
        i = j = k = 0
        while i<l_size and j<r_size:
            if left_arr[i] < right_arr[j]:
                li[k] = left_arr[i]
                i += 1
            else:
                li[k] = right_arr[j]
                j += 1
            k += 1
        while i < l_size:
            li[k] = left_arr[i]
            i += 1
            k += 1
        while j<r_size:
            li[k] = right_arr[j]
            j += 1
            k += 1
    return li

if __name__ == '__main__':
    li = [5,1,3,2,4]
    result = Merge_Sort(li)
    print(result)


