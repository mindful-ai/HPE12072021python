'''
    name = "anil"
    age = "35"
    sal = "10000000"
    tax = "10%"
    hike = "15%"

    caltax()

    calhike()

    printdetails()
'''
import math
def p():
    print("Outside Function!")

class employee:

    def __init__(self, n, a, s):
        self.name = n
        self.age  = a
        self.salary = s
        self.tax = 0
        self.hike = "0%"

    def calctax(self, pct):
        self.tax = self.salary * (pct/100)

    def calchike(self, hikepct):
        self.hike = math.ceil(self.salary * (float(hikepct[:-1])/100))
        self.salary = self.salary + self.hike
        self.calctax(10)

    def printdetails(self):
        print("NAME         : ", self.name)
        print("AGE          : ", self.age)
        print("-" * 50)
        print("GROSS SALARY : ", self.salary)
        print("NET SALARY   : ", self.salary - self.tax)
        p()

# ----------------------------------------------------------------------

"""
e1 = employee("Anil", 35, 1000000)
e1.printdetails()
e1.calctax(15)
e1.calchike("80%")
e1.printdetails()

"""

f = open("emp.csv")
d = f.readlines()
print(d)
f.close()

emps = []
for empdetails in d[1:]:
    L = empdetails.split(',')
    eobj = employee(L[0], int(L[1]), float(L[2].strip()))
    emps.append(eobj)

for emp in emps:
    emp.calctax(20)

for emp in emps:
    print(emp.printdetails())

f = open("report.csv", "w")
for emp in emps:
    s = ','.join([emp.name, str(emp.age), str(emp.salary), str(emp.tax), str(emp.hike)]) +'\n'
    f.write(s)
f.close()