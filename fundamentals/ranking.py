a = 4
b = 7
c = 8
if a > b:
    if a > c:
        print("a1", end=", ")
        if b > c:
            print("b2", end=", ")
            print("c3")
        else:
            print("c2", end=", ")
            print("b3")
    else:
        print("c1", end=", ")
        print("a2", end=", ")
        print("b3")
else:
    if b > c:
        print("b1", end=", ")
        if a > c:
            print("a2", end=", ")
            print("c3")
        else:
            print("c2", end=", ")
            print("a3")
    else:
        print("c1", end=", ")
        if a > b:
            print("a2", end=", ")
            print("b3")
        else:
            print("b2", end=", ")
            print("a3")

