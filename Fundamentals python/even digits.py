lst=[2,0,4,6,0,0,3,4]
res=[]
for i in lst:
    if i%2==0:
        if i not in res:
            res.append(i)
print(res)
