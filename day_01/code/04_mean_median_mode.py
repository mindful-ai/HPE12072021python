# For loop for taking inputs
# numbers and calculate the mean, median and mode of the numbers

# import statistics  => statistics.mean()

from statistics import mean, median, mode

# input
n = int(input("How many numbers: "))
print("-"*40)

# process

N = []
for i in range(n):
    x = float(input("# "))
    N.append(x)

# output
print("-"*40)
print("Entered Numbers: ", N)
print("MEAN           : ", mean(N))
print("Median         : ", median(N))
print("Mode           : ", mode(N))
