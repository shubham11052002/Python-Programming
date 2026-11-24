# name = input("Enter your name: ")
# print("Hello", name)

# age = int(input("Enter your age: "))
# print("Your age is:", age)


#   if we want to take multiple inputs in a single line...

a, b = map(int,input("Enter two values: ").split())

c = a + b;
print("Result is ",  c)