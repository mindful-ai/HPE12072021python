Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # TUPLES
>>> 
>>> L = ["red", "green", "blue"]
>>> T = ("red", "green", "blue")
>>> 
>>> type(L)
<class 'list'>
>>> type(T)
<class 'tuple'>
>>> 
>>> L[1] = "yellow"
>>> L
['red', 'yellow', 'blue']
>>> 
>>> T[1]
'green'
>>> T[1] = "yellow"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    T[1] = "yellow"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> # ------------------- Adding and removing elements not allowed
>>> 
>>> # ------------------- Rearranging
>>> 
>>> T
('red', 'green', 'blue')
>>> sorted(T)
['blue', 'green', 'red']
>>> T
('red', 'green', 'blue')
>>> reversed(T)
<reversed object at 0x0000027E389AEDA0>
>>> list(reversed(T))
['blue', 'green', 'red']
>>> 
>>> # --------------------- index, count
>>> 
>>> T
('red', 'green', 'blue')
>>> T.index('green')
1
>>> T.count('green')
1
>>> 
