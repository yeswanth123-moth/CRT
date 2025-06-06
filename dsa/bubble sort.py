def bubble_sort(a):
    for phase in range(1,len(a)):
        #phase 1 
        for i in range(len(a)-phase): #here phase=1 so 6-1=5 
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a         
a=[21,18,61,45,81,10]
print(bubble_sort(a))
#---------------------------------------------------
def bubble_sort(a):
    for phase in range(1,len(a)):
        flag=0
        #phase 1 
        for i in range(len(a)-phase): #here phase=1 so 6-1=5 
            if a[i]>a[i+1]:
                flag=1
                a[i],a[i+1]=a[i+1],a[i]
        if flag==0: #if flag remains zero then stop program and got to for loop phase
            break
    return a
a=[21,18,61,45,81,10]
print(bubble_sort(a))