# Program to determine how many years it takes to double the investment

# Input:  Principal = 10000
#         ROI       = 6.5 pa
# Output: 7.5 years

# Input

'''
Get the principal amount
Get the RoI pa 
'''
p = float(input("Principal        :"))
r = float(input("Rate of Interest :"))

# Process

'''
newamount = principal + (principal * roi)
principal = newamount
repeat the process 
    until principal = 2 times original principal
'''

finalamount = p
years = 0
while finalamount < (2 * p):
    finalamount = finalamount + (finalamount * (r/100))
    years += 1  # years = years + 1

# Output

'''
years = number of times the repeat happened
'''
print('-'*50)
print("It takes %d years for the amount to double" % years)