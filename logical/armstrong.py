num=12121
n=num
count=0
while n:
    n//=10
    count+=1
temp=num
dig=0
while temp:
    res=temp%10
    dig+=res**count
    temp=temp//10
print("armstrong" if dig==num else "not a armstrong")
