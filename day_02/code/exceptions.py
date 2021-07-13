'''
try:
    n = int(input("Enter a number: "))
    r = 100/n
except Exception as E:
    print("Divide by Zero not allowed! -> ", E)
else:
    print("RESULT: ", r)
finally:
    print("Thank you!")
'''

try:
    n = int(input("Enter a number: "))
    r = 100/n
    #s = "s" + 10
    D = {}
    #print(D["name"])
except ZeroDivisionError:
    print("Divide by Zero not allowed!")
except TypeError:
    print("Cannot use string and integer with +")
except Exception as E:
    print(E)
else:
    print("RESULT: ", r)
finally:
    print("Thank you!")