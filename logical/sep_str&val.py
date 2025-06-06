f="hkj38k22"
alpha=""
num=""
for l in f:
    if ('a'<=l<='z')or('A'<=l<='Z'):
        alpha=alpha+l
    elif '0'<=l<='9':
        num=num+l
print(alpha)
print(num)