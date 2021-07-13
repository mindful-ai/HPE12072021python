def timetaken(principal, roi, n):
    finalamount = principal
    years = 0
    while finalamount < (n * principal):
        finalamount = finalamount + (finalamount * (r/100))
        years += 1 
    return years  

# -------------------------------------------

# Input
# Principal = 1000000
# RoI       = 6.5
# Target    = 1.5
# Output
# ------------------------------------
# It takes 7 years to reach 1500000


# input
p = float(input("Principal     :"))
r = float(input("RoI           :"))
t = float(input("Target        :"))

# process
# output

print("It take %d years to reach %.2f" % (timetaken(p, r, t), (p * t)))