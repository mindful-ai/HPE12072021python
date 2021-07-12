Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LISTS
>>> 
>>> L = [1,2,3,1.4,-5,"red", "green", [1,2,3]]
>>> 
>>> 
>>> type(L)
<class 'list'>
>>> 
>>> L = ["red", "green", "blue"]
>>> 
>>> # -------------- Accessability
>>> 
>>> L[0]
'red'
>>> L[-1]
'blue'
>>> L[1:3]
['green', 'blue']
>>> L[::-1]
['blue', 'green', 'red']
>>> 
>>> # ----------------- Mutability
>>> 
>>> L
['red', 'green', 'blue']
>>> L[1]
'green'
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> 
>>> L[1]
'yellow'
>>> L[1][1]
'e'
>>> L[1][1] = "m"
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    L[1][1] = "m"
TypeError: 'str' object does not support item assignment
>>> 
>>> # ------------------ Add elements
>>> 
>>> L
['red', 'yellow', 'blue']
>>> L.append("green")
>>> L
['red', 'yellow', 'blue', 'green']
>>> L.append("brown")
>>> L.insert(1, "golden")
>>> L
['red', 'golden', 'yellow', 'blue', 'green', 'brown']
>>> 
>>> L1 = ["black", "grey", "white"]
>>> 
>>> L[-1] = L1
>>> L
['red', 'golden', 'yellow', 'blue', 'green', ['black', 'grey', 'white']]
>>> 
>>> 
>>> L = ['red', 'golden', 'yellow', 'blue', 'green', 'brown']
>>> L.append(L1)
>>> L
['red', 'golden', 'yellow', 'blue', 'green', 'brown', ['black', 'grey', 'white']]
>>> L.insert(1, L1)
>>> L
['red', ['black', 'grey', 'white'], 'golden', 'yellow', 'blue', 'green', 'brown', ['black', 'grey', 'white']]
>>> 
>>> 
>>> L = ['red', 'golden', 'yellow', 'blue', 'green', 'brown']
>>> L.extend(L1)
>>> L
['red', 'golden', 'yellow', 'blue', 'green', 'brown', 'black', 'grey', 'white']
>>> 
>>> 
>>> L = L = ['red', 'golden', 'yellow', 'blue', 'green', 'brown']
>>> L
['red', 'golden', 'yellow', 'blue', 'green', 'brown']
>>> 
>>> L1
['black', 'grey', 'white']
>>> L[1]
'golden'
>>> # L[1] = L
>>> 
>>> L[1:2]
['golden']
>>> L[1:2] = L1
>>> L
['red', 'black', 'grey', 'white', 'yellow', 'blue', 'green', 'brown']
>>> 
>>> 
>>> # ----------------- Removing elements
>>> 
>>> L
['red', 'black', 'grey', 'white', 'yellow', 'blue', 'green', 'brown']
>>> L.pop()
'brown'
>>> L
['red', 'black', 'grey', 'white', 'yellow', 'blue', 'green']
>>> L.pop()
'green'
>>> L
['red', 'black', 'grey', 'white', 'yellow', 'blue']
>>> L.pop(2)
'grey'
>>> L
['red', 'black', 'white', 'yellow', 'blue']
>>> L.remove('white')
>>> L
['red', 'black', 'yellow', 'blue']
>>> 
>>> # ------------------------ re-arrange elements
>>> 
>>> sorted(L)
['black', 'blue', 'red', 'yellow']
>>> L
['red', 'black', 'yellow', 'blue']
>>> reversed(L)
<list_reverseiterator object at 0x000001D75C21ED68>
>>> list(reversed(L))
['blue', 'yellow', 'black', 'red']
>>> L
['red', 'black', 'yellow', 'blue']
>>> 
>>> L.sort()
>>> L
['black', 'blue', 'red', 'yellow']
>>> 
>>> L.reverse()
>>> L
['yellow', 'red', 'blue', 'black']
>>> 
>>> 
>>> # --------------------- finding elements
>>> 
>>> L
['yellow', 'red', 'blue', 'black']
>>> 'red' in L
True
>>> L.index('red')
1
>>> L.count('red')
1
>>> 
>>> # -------------------- iterations
>>> 
>>> for item in L:
	print(item)

	
yellow
red
blue
black
>>> 
>>> for item in L:
	print(item, ' --> ', len(item))

	
yellow  -->  6
red  -->  3
blue  -->  4
black  -->  5
>>> 
>>> # -------------------- copying a list
>>> 
>>> L
['yellow', 'red', 'blue', 'black']
>>> L1 = L
>>> L1
['yellow', 'red', 'blue', 'black']
>>> L1[1] = "orange"
>>> L1
['yellow', 'orange', 'blue', 'black']
>>> L
['yellow', 'orange', 'blue', 'black']
>>> 
>>> import copy
>>> L
['yellow', 'orange', 'blue', 'black']
>>> L1 = copy.deepcopy(L)
>>> L
['yellow', 'orange', 'blue', 'black']
>>> L1
['yellow', 'orange', 'blue', 'black']
>>> L1[1] = "red"
>>> L1
['yellow', 'red', 'blue', 'black']
>>> L
['yellow', 'orange', 'blue', 'black']
>>> 
>>> 
>>> 
>>> # ----------------- Soumya
>>> 
>>> L
['yellow', 'orange', 'blue', 'black']
>>> L1
['yellow', 'red', 'blue', 'black']
>>> 
>>> 
>>> 
>>> # ------------------------------
>>> 
>>> for c in "aeiou":
	print(c)

	
a
e
i
o
u
>>> 
= RESTART: C:/Users/Purushotham/Desktop/hp/day_01/code/03_for_loop_vowels.py =
Enter some text: This is to test the vowels exervise
a  --->  0
e  --->  6
i  --->  3
o  --->  2
u  --->  0
>>> 
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(10,20))
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> list(range(10, 30, 2))
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
>>> list(range(10, 1, -1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
>>> 
