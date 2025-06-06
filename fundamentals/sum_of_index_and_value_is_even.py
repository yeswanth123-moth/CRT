a=[2,3,5,7,8,9]
for i in range(len(a)):
    res=(i+a[i])
    if res%2==0:
        print(res,end=" ")