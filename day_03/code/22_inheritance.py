class student:

    # class variables
    nstudents = 0
    schoolname = ''

    # Data/attributes
    def __init__(self, name, cls, rid):
        print('Initializing values.....')
        self.name = name
        self.cls = cls
        self.regid = rid
        self.physics = 0
        self.maths = 0
        self.chemistry = 0
        self.biology = 0
        self.average = 0
        student.nstudents += 1

    # Functions/methods

    def setschoolname(self, schoolname):
        student.schoolname = schoolname

    def printinfo(self):
        self.state = 'Karnataka'
        print('STATE : ', self.state)
        print('SCHOOL: ', student.schoolname)
        print('-----------------------------------')
        print('NAME: ', self.name)
        print('CLASS: ', self.cls)
        print('REG ID:', self.regid)
        print('-----------------------------------')
        print('MATHS    : ', self.maths)
        print('PHYSICS  : ', self.physics)
        print('CHEMISTRY: ', self.chemistry)
        print('BIOLOGY  : ', self.biology)
        print('-----------------------------------')
        print('AVERAGE  : ', self.average)
        print('NSTUDENTS  ------> ', student.nstudents)
        print('\n')

    def setMaths(self, marks):
        self.maths = marks

    def setPhysics(self, marks):
        self.physics = marks

    def setChemistry(self, marks):
        self.chemistry = marks

    def setBiology(self, marks):
        self.biology = marks

    def calcAverage(self):
        self.average = (self.physics + self.chemistry + self. biology + self.maths)/4


#######################################################################################

class newstudent(student):
    pass

class ext_student(student):

    # Attributes
    def __init__(self, name, cls, rid, native, extra=['music']):
        super().__init__(name, cls, rid) # initializing the parent with appropriate data
        self.native = native # New attribute
        self.extra = extra   # New attribute

    # Functions
    def getGrade(self): # New function in the extended class
        if(self.average > 90):
            return 'A+'
        elif(70 < self.average < 90):
            return 'A'
        elif(50 < self.average < 70):
            return 'B'
        else:
            return 'C'


    def printinfo(self):  # Overriding the function
        super().printinfo()
        print('-----------------------------------')
        print('Native : %s' % self.native)
        print('Extras : ', self.extra)
        print('Grade  : %s' % self.getGrade())



class ext_student2(ext_student):

    # Attributes
    def __init__(self, name, cls, rid, native, extra=['music'], addr='JP nagar, BLR'):
        super().__init__(name, cls, rid, native, extra) # initializing the parent with appropriate data
        self.addr = addr
        self.city = city


#######################################################################################
s1 = newstudent('Rohit', 12, 'A001')
s1.printinfo()




s1 = ext_student('Rohit', 12, 'A001', 'Bellary',['Hockey','Travel'])
s1.printinfo()
print('\n\n')

s1.setPhysics(100)
s1.setMaths(99)
s1.setChemistry(98)
s1.setBiology(97)
s1.printinfo()
print('\n\n')

s1.calcAverage()
s1.printinfo()


