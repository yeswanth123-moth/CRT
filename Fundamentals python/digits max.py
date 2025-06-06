a = [1, 2, 3, 7678, 5, 87, 456]
mx = a[0]
for i in range(1, len(a)):
    if a[i] > mx:
        mx = a[i]
print("Maximum:", mx)
