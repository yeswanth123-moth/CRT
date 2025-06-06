n=12123
res=0
temp=n
while temp:
   rem=temp%10
   res=(res*10)+rem
   temp=temp//10
print("palindrome" if res==n else "not a palindrome")
 
