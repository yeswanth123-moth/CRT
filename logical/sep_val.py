l=999

while l>9:
    sum=0
    while l>0:
        sum+=l%10
        l //=10
    l=sum
print(l)