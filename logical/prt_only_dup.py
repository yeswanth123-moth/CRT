lst=[2,0,4,6,0,0,3,4]
res=[]
rem=[]
for i in lst:
    if i not in res:
        res.append(i)
    else:
        rem.append(i)
print("duplicates are:",rem)
