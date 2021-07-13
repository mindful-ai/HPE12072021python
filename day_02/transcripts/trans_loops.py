Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Loops
>>> 
>>> # Multiplication table
>>> 
>>> # 5 X 1 = 5
>>> # 5 X 2 = 10
>>> 
>>> print(5, ' X ', 1, ' = ', (5*1))
5  X  1  =  5
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> i = 1
>>> while i <= 10:
	print(5, ' X ', i, ' = ', (5*i))
	i = i + 1

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> 
>>> L = ["red", "green", "blue", "yellow"]
>>> for item in L:
	print(item, end=' ')

	
red green blue yellow 
>>> for item in L:
	print(item)

	
red
green
blue
yellow
>>> s = "python"
>>> for c in s:
	print(c.upper(), end='-')

	
P-Y-T-H-O-N-
>>> 
>>> # -------------------------------- Loop Controls
>>> 
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> for i in range(1, 11):
	if(i == 5):
		break
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
>>> 
>>> 
>>> for i in range(1, 11):
	print(5, ' X ', i, ' = ', (5*i))
	if(i == 5):
		break

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  5  =  25
>>> 
>>> 
>>> for i in range(1, 11):
	if(i == 5):
		continue
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  3  =  15
5  X  4  =  20
5  X  6  =  30
5  X  7  =  35
5  X  8  =  40
5  X  9  =  45
5  X  10  =  50
>>> 
>>> for i in range(1, 11):
	if(i % 3 == 0):
		continue
	print(5, ' X ', i, ' = ', (5*i))

	
5  X  1  =  5
5  X  2  =  10
5  X  4  =  20
5  X  5  =  25
5  X  7  =  35
5  X  8  =  40
5  X  10  =  50
>>> 
>>> # ------------------------ Loop else block
