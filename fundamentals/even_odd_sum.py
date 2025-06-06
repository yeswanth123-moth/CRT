a=[1,2,3,4,5,6,7,8]
s1=0
s2=0
for i in range(len(a)):
    if a[i]%2==0:
        s1+=i
    else:
        s2+=i
print(s1,s2)
if s1>s2:
    print("even")
else:
    print("odd")