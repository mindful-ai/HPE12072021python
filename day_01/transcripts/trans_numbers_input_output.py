Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> 5 + 4
9
>>> 6 + 7
13
>>> 2 * 7
14
>>> # ------------------------ NUMBERS ------------------- #
>>> # 5, +5, -4, 5.6, ..
>>> a = 5
>>> print(a)
5
>>> type(a)
<class 'int'>
>>> b = 5.6
>>> type(b)
<class 'float'>
>>> c = ''
>>> type(c)
<class 'str'>
>>> 
>>> 
>>> # --------------- Operators
>>> 
>>> # Arithmetic operator
>>> 
>>> a
5
>>> b
5.6
>>> a + b
10.6
>>> a - 2
3
>>> a * 4
20
>>> a / 5
1.0
>>> a % 3
2
>>> a // 3
1
>>> a ** 2
25
>>> 
>>> # Relational operators
>>> 
>>> a > 6 # Is a greater than 6?
False
>>> a < 6
True
>>> a >= 6
False
>>> a <= 6
True
>>> a == 5
True
>>> a != 6
True
>>> 
>>> # Logical opertors
>>> 
>>> (a > 5)
False
>>> a < 5
False
>>> a == 5
True
>>> a > 4 and a == 5
True
>>> a < 6 or a > 4
True
>>> a < 6 or a > 7
True
>>> a < 6 and a > 7
False
>>> not(a < 6 or a > 7)
False
>>> a < 6 and not a > 7
True
>>> 
>>> # ----------------------- in-built functions
>>> 
>>> a = 100
>>> type(a)
<class 'int'>
>>> hex(a)
'0x64'
>>> bin(a)
'0b1100100'
>>> oct(a)
'0o144'
>>> 
>>> a = "10456"
>>> # a = a + a * 0.15
>>> a = a + (a * 0.15)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a = a + (a * 0.15)
TypeError: can't multiply sequence by non-int of type 'float'
>>> a = int(a) + (int(a) * 0.15)
>>> a
12024.4
>>> 
>>> a = 5
>>> b = 2
>>> pow(a, b)
25
>>> pow(a, b, 4)
1
>>> # -------------------------- built in modules
>>> 
>>> a = 77
>>> a ** 2
5929
>>> a ** 0.5
8.774964387392123
>>> 
>>> gcd(10, 20)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    gcd(10, 20)
NameError: name 'gcd' is not defined
>>> 
>>> import math
>>> math.gcd(10, 20)
10
>>> math.lcm(10, 20)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    math.lcm(10, 20)
AttributeError: module 'math' has no attribute 'lcm'
>>> math.lcm(10, 20, 30)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    math.lcm(10, 20, 30)
AttributeError: module 'math' has no attribute 'lcm'
>>> 
>>> math.sqrt(144)
12.0
>>> 
>>> 
>>> import random
>>> random.randint(1, 100)
3
>>> random.randint(1, 100)
68
>>> random.randint(1, 100)
62
>>> random.randint(1, 100)
8
>>> random.randint(1, 100)
85
>>> random.randint(1, 100)
98
>>> 
>>> # -------------------- ouput
>>> 
>>> a
77
>>> print("The square root of a is ", math.sqrt(a))
The square root of a is  8.774964387392123
>>> 
>>> 
>>> # ----------------------- input
>>> 
>>> input()
903248
'903248'
>>> c = input()
123
>>> c
'123'
>>> int(c) + 100
223
>>> int(c)
123
>>> c = input("Enter a number: ")
Enter a number: 45
>>> print(c)
45
>>> math.pow(c, 4)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    math.pow(c, 4)
TypeError: must be real number, not str
>>> math.pow(int(c), 4)
4100625.0
>>> 
