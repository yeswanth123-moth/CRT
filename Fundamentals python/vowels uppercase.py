a='abcdefghi'
for i in a:
    if i in 'aeiou':
        print(chr(ord(i)-32),end=" ")
    else:
        print(i,end=" ")
