a=[0,2,3,7678,5,87,456]
mn=a[0]
for i in range(1,len(a)):
    if a[i]<mn:
        mn=a[i]
print(mn)
