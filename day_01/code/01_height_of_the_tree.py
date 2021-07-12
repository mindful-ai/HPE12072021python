# Program to calculate the height of the treee


# Input:
# Enter the distance(M) : 10
# Enter the angle(D)    : 60
# Output:
# ------------------------------
# Height of the tree    : N ft

import math

C_FEET =  3.2808399

# Input
dist = input("Enter the distance(M) :")
ang  = float(input("Enter the angle(D)    :"))

# Process
# h = d tan(a)

dist = float(dist)
h = dist * math.tan(math.radians(ang))
h = h * C_FEET

# Output

print("-----------------------------------")
#print("Height of the tree    :", h, " ft")
print("Height of the tree    : %.2f ft" % h)
