# Develop a guess my number game

'''
-------------------------------------------
    WELCOME TO GUESS NUMBER
-------------------------------------------

Computer has randomly picked up a number (45)
Can you guess that?

-> 10
Incorrect. Guess higher
-> 55
Incorrect. Guess Lower
-> 45
Congratulations!

You took 3 trials at it is excellent playing!

'''

import random

print("-------------------------------------------")
print("      WELCOME TO GUESS NUMBER              ")
print("-------------------------------------------")

print("Computer has randomly picked up a number between 1 and 100")
print("Can you guess that?\\n")

# Malvika -> rn = function to pick a random number
rn = random.randint(1, 100)
#print("[RN]", rn)

# initialize trials = 0
trials = 0

# Loop (infinite)
while True:

    # trials == 10; break
    if(trials == 10):
        break

    # Shankar -> ui = Get user input
    ui = int(input("-> Guess ? "))
    
    #print("[UI]", ui)
    # compare rn and ui
    # ui > rn message -> guess something lower; trials ++
    if(ui > rn):
        print("Incorrect. Guess lower")
        trials += 1
    # ui < rn message -> guess something higher; trials ++
    elif(ui < rn):
        print("Incorrect. Guess higher")
        trials += 1
    # ui == rn message -> congratulations; break
    else:
        print("Congratulations!!!")
        break

# Output the results
print("-------------------------------------------")
if(trials < 5):
    print("Excellent Playing")
elif(5 < trials < 8):
    print("Good Playing")
else:
    print("Needs Improvement...")