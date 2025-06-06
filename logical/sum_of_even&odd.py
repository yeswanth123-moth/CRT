l=(20,10,28,37,74,98,31)
odd=0
even=0
for i in range(len(l)):
    if i%2==0:
        even=even+l[i]
    else:
        odd=odd+l[i]

if even<odd:
    print(odd)
else:
    print(even)
     #-------------------------------------
a=[5,24,45,3]
even=odd=0
for i in range(1,len(a),2):
    even+=a[i-1]
    odd+=a[i]
if (len(a)-1)%2==0:even+=a[-1]
print("even" if even>odd else odd)
