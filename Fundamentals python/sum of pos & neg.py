lst = [2,4,6,-10,3,-4]
sum1=0
sum2=0
for i in lst:
    if i<0:
        sum1+=i
    else:
        sum2+=i
print(sum1,sum2)
