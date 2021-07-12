Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # ---------------- STRINGS -------------
>>> 
>>> s = "python"
>>> type(s)
<class 'str'>
>>> 
>>> 
>>> # ------------------------ Sub-scripting
>>> # s[index]
>>> s[0]
'p'
>>> s[1]
'y'
>>> s[3]
'h'
>>> s[-1]
'n'
>>> s[-2]
'o'
>>> # s[start:end]
>>> s[1:3]
'yt'
>>> s[2:5]
'tho'
>>> s[-5:-1]
'ytho'
>>> 
>>> s[0:3]
'pyt'
>>> s[:3]
'pyt'
>>> s[3:]
'hon'
>>> s[:]
'python'
>>> 
>>> # s[start:end:skip]
>>> s
'python'
>>> s[2:5]
'tho'
>>> s[1:5]
'ytho'
>>> s[1:5:1]
'ytho'
>>> s[1:5:2]
'yh'
>>> s[1:5:3]
'yo'
>>> 
>>> s = "computer"
>>> s[1:6:2]
'opt'
>>> s[1:7:3]
'ou'
>>> 
>>> s[:]
'computer'
>>> s[::2]
'cmue'
>>> s[1::2]
'optr'
>>> 
>>> 
>>> s[::-1]
'retupmoc'
>>> s[::1]
'computer'
>>> s[::-2]
'rtpo'
>>> 
>>> # ---------------------- Immutability
>>> 
>>> s
'computer'
>>> s[2]
'm'
>>> s[2] = "x"
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    s[2] = "x"
TypeError: 'str' object does not support item assignment
>>> 
>>> # -------------------- operators
>>> 
>>> "abc" + "def"
'abcdef'
>>> s
'computer'
>>> s[:3] + 'x' + s[4:]
'comxuter'
>>> 
>>> "abc" * 3
'abcabcabc'
>>> 
>>> a = "python"
>>> a = a[4:]
>>> a
'on'
>>> a[4:] = a
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a[4:] = a
TypeError: 'str' object does not support item assignment
>>> a[4:] = "er"
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a[4:] = "er"
TypeError: 'str' object does not support item assignment
>>> # ----------- Malvika
>>> 
>>> s
'computer'
>>> y = s
>>> y
'computer'
>>> 
>>> # -----------
>>> 
>>> 
>>> s
'computer'
>>> "put" in s
True
>>> s is str
False
>>> type(s) is str
True
>>> type(s) is int
False
>>> isinstance(s, str)
True
>>> type(s)
<class 'str'>
>>> 
>>> len(s)
8
>>> del s
>>> s
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> 
>>> # ------------------------- Operations on strings
>>> 
>>> # Functions
>>> 
>>> # CASE Related
>>> 
>>> s
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    s
NameError: name 's' is not defined
>>> s = "computer'
SyntaxError: EOL while scanning string literal
>>> s = 'computer'
>>> s.upper()
'COMPUTER'
>>> s
'computer'
>>> s1 = s.upper()
>>> s1
'COMPUTER'
>>> s
'computer'
>>> s = s.upper()
>>> s
'COMPUTER'
>>> s = s.lower()
>>> s
'computer'
>>> s.capitalize()
'Computer'
>>> 
>>> # QUERY a string
>>> 
>>> s.isupper()
False
>>> s
'computer'
>>> s.islower()
True
>>> s.isspace()
False
>>> s.isdigit()
False
>>> '1234'.isdigit()
True
>>> s.isalpha()
True
>>> s.isalnum()
True
>>> '213dsf*&*'.isalnum()
False
>>> 
>>> 
>>> # Seraching in the string
>>> 
>>> s
'computer'
>>> s.index('p')
3
>>> s.lindex('p')
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    s.lindex('p')
AttributeError: 'str' object has no attribute 'lindex'
>>> s.rindex('p')
3
>>> s ="computputer"
>>> s.index('p')
3
>>> s.rindex('p')
6
>>> s.find('p')
3
>>> s.rfind('p')
6
>>> s.index('a')
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    s.index('a')
ValueError: substring not found
>>> s.find('a')
-1
>>> 
>>> 
>>> # --------- Poornima
>>> 
>>> s = "python"
>>> s.capitalize()
'Python'
>>> s
'python'
>>> S
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    S
NameError: name 'S' is not defined
>>> 
>>> 
>>> s
'python'
>>> s = "mississippi"
>>> s.count('s')
4
>>> s.count("ss")
2
>>> 
>>> # ------------------------ Modificaitons on the string

>>> s
'mississippi'
>>> 
>>> # Justification
>>> 
>>> s.ljust(30)
'mississippi                   '
>>> s.rjust(30, '.')
'...................mississippi'
>>> 
>>> # Replacement
>>> 
>>> ip = '192-78-2-1'
>>> ip.replace('-', '.')
'192.78.2.1'
>>> 
>>> amt = '16,45,789'
>>> int(amt)
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    int(amt)
ValueError: invalid literal for int() with base 10: '16,45,789'
>>> float(amt)
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    float(amt)
ValueError: could not convert string to float: '16,45,789'
>>> int(amt.replace(',',''))
1645789
>>> int(amt.replace(',','')) * 0.33
543110.37
>>> 
>>> # Querying
>>> 
>>> url = "www.google.com"
>>> url.startswith("https")
False
>>> url.endswith("com")
True
>>> 
>>> 
>>> # Split and Join
>>> 
>>> s = "mary had a little lamb"
>>> s.split()
['mary', 'had', 'a', 'little', 'lamb']
>>> s.split('a')
['m', 'ry h', 'd ', ' little l', 'mb']
>>> 
>>> L = s.split('a')
>>> L
['m', 'ry h', 'd ', ' little l', 'mb']
>>> type(L)
<class 'list'>
>>> 'A'.join(L)
'mAry hAd A little lAmb'
>>> 
>>> 
>>> 
>>> # ------------------- Balaji
>>> 
>>> a = "computer"
>>> b = a.split('u')[1]
>>> b
'ter'
>>> 
