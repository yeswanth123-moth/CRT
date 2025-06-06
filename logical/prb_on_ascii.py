a=[19, 9, 14, 4, 8, 21]
sum=' '
for i in a:
    sum+=(chr(i+96))
print(sum)

a='abcdefghi'
for i in a:
    if i in 'aeiou':
        print(chr(ord(i)-32),end=" ")
    else:
        print(i,end=" ")
        

a='govind'
sum=0
for i in a:
    sum+=(ord(i)-96)
print(sum)

a=[19, 9, 14, 4, 8, 21]
sum=''
for i in a:
    sum+=(chr(i+96))
print(sum)

