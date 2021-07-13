# Program to determine if a number is prime or not

# Input
n = int(input("Enter an number: "))

# Process/Output

for i in range(2, n):
    if(n % i == 0):
        print("The number is not prime")
        break
else:
    print("The number is prime")

# Loops exit because of two reasons
# 1. Natural exit
# 2. Break
# If there is a natural exit, else block executes once
# If the loop exits because of break, else block doesnot execute