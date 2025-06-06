n=10
a,b=0,1
print(a,b,end=' ')
for i in range(n-2):
   fib=a+b
   print(fib,end=' ')
   a,b=b,fib
