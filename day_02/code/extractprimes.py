# Input "some" numbers from the users
# Extract all the prime numbers from the inputs

'''
Inputs:

# 12
# 13
# 55
# 17
# wqewr
# dsfg
# q!

Outputs:

--------------------------------------
Entered numbers: 12 13 55 17
Extracted primes: 13 17

'''

import myprime 
# from myprime import checkprime

# Input

'''
Declaring a empty container
Receive an input
If the input is a number load it into the container
Repeat the process until q! is entered
'''
N = []
while True:

    uin = input("# ")

    if(uin == 'q!'):
        break
    else:
        if(uin.isdigit()):
            N.append(int(uin))


# Process

'''
define another container to contain prime numbers say primes
iterate all the numbers in the main container
if the number is prime, load it into primes
'''
primes = []
for n in N:
    if(myprime.checkprime(n)):
        primes.append(n)

# Output

'''
print the numbers in main and primes containers
'''
print('-'*50)
print('Numbers Entered  : ', N)
print('Primes Extracted : ', primes)