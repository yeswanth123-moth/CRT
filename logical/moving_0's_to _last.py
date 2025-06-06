lst=[2,0,4,6,0,0,3,4]
for i in range(len(lst)):
    if lst[i]==0:
        lst.remove(0)
        lst.append(0)
print(lst)
