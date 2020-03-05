def shellsort(arr):

    n= len(arr)
    gap = n//2

    while gap >0:

        for i in range(gap,n):
            temp = arr[i]
            j=i
        while j>=gap and arr[j-gap]>temp:
            arr[j] = arr[j-gap]
            j= j-gap

        j=j-gap

    gap = gap//2

    return arr