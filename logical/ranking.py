a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a > b and a > c:
    if b > c:
        print("a1 b2 c3")
    else:
        print("a1 c2 b3")
elif b > c:
    if a > c:
        print("b1 a2 c3")
    else:
        print("b1 c2 a3")
else:
    if a > b:
        print("c1 a2 b3")
    else:
        print("c1 b2 a3")
