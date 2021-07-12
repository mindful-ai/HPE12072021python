# Program to subtract two number

# input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# process

res = a - b

# output

print("-"*60)
print("DIFFERENCE: ", abs(a - b))
if(res > 0):
    print("The result is positive")
elif(res < 0):
    print("The result is negative")
else:
    print("The result is zero")

    
