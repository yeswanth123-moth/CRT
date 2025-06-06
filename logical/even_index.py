# Printing only even numbers in list
lst=[2,0,4,6,0,0,3,4]
res=[]
for i in lst:
    if i%2==0:
        if i not in res:
            res.append(i)
print(res)
# Printing only even index values:
lst=[2,0,4,6,0,0,3,4]
for i in range(0,len(lst),2):
        print(lst[i])