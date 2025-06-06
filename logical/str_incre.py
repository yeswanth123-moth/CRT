n = 1452
n = str(n)
prev = 0
for next in range(len(n)):
    if int(n[next]) <= prev:
        break
    prev = int(n[next])
else:
    next += 1
print(next)
#______________________________________________________
a = 12672

# Step 1: Extract digits without using str()
digits = []
while a > 0:
    digits.append(a % 10)
    a = a // 10

# Step 2: Reverse to correct order
digits.reverse()

# Step 3: Compare and print increasing sequence
print(digits[0])  # Always print the first digit
for i in range(1, len(digits)):
    print(digits[i])
    if digits[i] <= digits[i - 1]:
        break
