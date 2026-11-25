a = 10
b = 3

# Arithmetic
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Comparison
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

# Logical
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))

# Assignment
a += 5
print(a)

# Membership
names = ["Rahul", "Amit", "Shubham"]
print("Amit" in names, "Raj" not in names)

# Identity
x = names
y = ["Rahul", "Amit", "Shubham"]
print(names is x, names is y)

# Bitwise
print(5 & 3, 5 | 3, 5 ^ 3, ~5, 5 << 1, 5 >> 1)


num1 = 5;
num2 =4;
print(bin(5 & 4))