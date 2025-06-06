def binary_search(a,key):
    s=0
    e=len(a)-1
    while s<=e: #checks until start crosses end
        mid=(s+e)//2
        if a[mid]==key: #a[mid] means it takes value of that index =12(3rd index)
            return mid
        elif a[mid]>key:
            e=mid-1
        else:
            s=mid+1
        
a=[5,8,10,12,41,45,81,108]
print(binary_search(a,8)) 