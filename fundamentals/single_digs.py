def print_if_less_than_10(a, index=0):
    if index == len(a):
        return
    if a[index] < 10:
        print(a[index], end=" ")
    print_if_less_than_10(a, index + 1)

# Call the function with the list
a = [2, 34, 56, 7, 8, 9]
print_if_less_than_10(a)