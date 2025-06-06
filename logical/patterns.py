# n=5
# for i in range(1,n+1):
#     print("*"*i)
#reverse star
# n=5
# for i in range(n,0,-1):
#     print("*"*i)
#
# n=5
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*i)
#
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#n=5
# for i in range(n,0,-1):
#     print("  "*(n-i)+"* "*i)
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range(1,n):
#     print("  "*(n-i)+"* "*i)
# for i in range(n,0,-1):
#     print("  "*(n-i)+"* "*i)
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i)+"* "*i)
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# n=5(diamond)
# for i in range(1,n):
#     print(" "*(n-i)+"* "*i)
# for i in range(n,0,-1):
#     print(" "*(n-i)+"* "*i)
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# n=9(square)
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n:
#             print("* ",end=" ")
#         else:
#             print("  ",end=" ")
#     print()
# n=5(sqaure)
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("* "*n)
#     else:
#         print("* "+"  "*(n-2)+"*")
#         * * * * *
#         *       *
#         *       *
#         *       *
#         * * * * *
# n=5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print( )
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# n=5
# for i in range(1,n+1):
#      for j in range(1,i+1):
#         print(j,end=" ")
#      print( )
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n or i==j or (i+j)==(n+1):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# * * * * *
# * *   * *
# *   *   *
# * *   * *
# * * * * *

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if  i==j or (i+j)==(n+1):
#             print("* ",end="")
#         else:
#             print("  ",end="")
#     print()
# *       *
#   *   *
#     *
#   *   *
# *       *
# n=5
# for i in range(1,n+1):
#     for j in range(0,i):
#         print(chr(ord("a")+j),end=" ")
#
#     print( )

# a
# a b
# a b c
# a b c d
# # a b c d e
# n=5
# for i in range(1,n+1):
#     for j in range(0,i+1):
#         print(chr((ord("a")-1)+i),end=" ")
#     print( )
#
# a
# b b
# c c c
# d d d d
# e e e e e
# s="govind"
# for i in range(1,len(s)):
#     print(s[:i])
# for i in range(len(s),0,-1):
#     print(s[:i])
# g
# go
# gov
# govi
# govin
# govind
# govin
# govi
# gov
# go
# g

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(chr(ord("a")+i),end=" ")
#     print()
n=int(input())
elements=list(map(int,input().split()))
key=int(input())
for items in elements:
    if items==key:
        found=True
        break
if found==True:
    print("value found")
else:
    print("value not found")


