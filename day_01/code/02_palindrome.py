# Program to determine if a string is palidrome or not
# Ex: madam

# input

s = input("Enter a string: ")

# process
# output

if(s == s[::-1]):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
    
