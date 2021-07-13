Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # SETS
>>> 
>>> s = "mississippi"
>>> list(s)
['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> tuple(s)
('m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i')
>>> set(s)
{'m', 'i', 'p', 's'}
>>> 
>>> # ----------------- operators
>>> 
>>> s1 = set("abcdef")
>>> s1
{'a', 'c', 'f', 'b', 'e', 'd'}
>>> s2 = {'d', 'e', 'f', 'g', 'h', 'i'}
>>> s2
{'f', 'e', 'i', 'h', 'd', 'g'}
>>> 
>>> s1 & s2
{'e', 'd', 'f'}
>>> s1 | s2
{'a', 'c', 'f', 'b', 'e', 'i', 'd', 'h', 'g'}
>>> s1 ^ s2
{'a', 'c', 'h', 'b', 'i', 'g'}
>>> 
>>> # --------------------- in-built functions
>>> 
>>> s
'mississippi'
>>> s1
{'a', 'c', 'f', 'b', 'e', 'd'}
>>> s1.add('x')
>>> s1
{'a', 'c', 'x', 'f', 'b', 'e', 'd'}
>>> s3 = {'y', 'z'}
>>> s1.update(s3)
>>> s1
{'y', 'a', 'c', 'z', 'x', 'f', 'b', 'e', 'd'}
>>> 
>>> 'z' in S1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    'z' in S1
NameError: name 'S1' is not defined
>>> 'z' in s1
True
>>> s1.remove('z')
>>> s1
{'y', 'a', 'c', 'x', 'f', 'b', 'e', 'd'}
>>> 
