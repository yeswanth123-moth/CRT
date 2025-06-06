def Merge_sort(arr):
    if len(arr)==1:
         return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    Merge_sort(left)
    Merge_sort(right)

    k = i= j =0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k] = left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j < len(right):
        arr[k] = right[j]
        j+=1
        k+=1
a = [ 21 ,18,61,45,81,10]
Merge_sort(a)
print(a)
