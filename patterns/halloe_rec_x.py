n=9
for i in range(1,10):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n or i==j or (i+j)==(n+1):
            print("* ",end="")
        else:
            print("  ",end="")
    print()
    