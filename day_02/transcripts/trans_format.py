Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "My name is {} and age is {}".format("Anil", 35)
'My name is Anil and age is 35'
>>> "My name is {0} and age is {1}".format("Anil", 35)
'My name is Anil and age is 35'
>>> "My name is {0:10} and age is {1:5}".format("Anil", 35)
'My name is Anil       and age is    35'
>>> "My name is {0:>10} and age is {1:<5}".format("Anil", 35)
'My name is       Anil and age is 35   '
>>> "My name is {0:^10} and age is {1:^5}".format("Anil", 35)
'My name is    Anil    and age is  35  '
>>> 
>>> template = '''My name is {0:^10}
age is {1:^5}'''
>>> print(template.format('sunil', 45))
My name is   sunil   
age is  45  
>>> template = '''My name is {name:^10}
age is {age:^5}'''
>>> print(template.format(name='sunil', age=45))
My name is   sunil   
age is  45  
>>> 
