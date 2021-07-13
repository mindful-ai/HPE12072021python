Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Files
>>> 
>>> 
>>> # open(), close()
>>> # read(), readline(), readlines()
>>> # tell(), seek()
>>> # write(), writelines()
>>> 
>>> path = "C:\Users\Purushotham\Desktop\hp\day_02\code\colors.txt"
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> path = r"C:\Users\Purushotham\Desktop\hp\day_02\code\colors.txt"
>>> 
>>> f = open(path, "r")
>>> content - f.read()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    content - f.read()
NameError: name 'content' is not defined
>>> content = f.read()
>>> content
'red\ngreen\nblue\nyellow\ngolden\nmaroon\ncyan\nmagenta\n'
>>> print(content)
red
green
blue
yellow
golden
maroon
cyan
magenta

>>> type(content)
<class 'str'>
>>> f.readline()
''
>>> f.tell()
57
>>> len(content)
49
>>> f.seek(0)
0
>>> f.tell()
0
>>> f.readline()
'red\n'
>>> f.readline()
'green\n'
>>> f.readline()
'blue\n'
>>> f.read(15)
'yellow\ngolden\nm'
>>> f.seek(0)
0
>>> f.readlines()
['red\n', 'green\n', 'blue\n', 'yellow\n', 'golden\n', 'maroon\n', 'cyan\n', 'magenta\n']
>>> 
>>> # -------------------------- write into file
>>> f.close()
>>> 
>>> path = r"C:\Users\Purushotham\Desktop\hp\day_02\code\colors2.txt"
>>> f = open(path, "w")
>>> f.write("My colors\n------------------\n\n")
30
>>> f.close()
>>> 
>>> content
'red\ngreen\nblue\nyellow\ngolden\nmaroon\ncyan\nmagenta\n'
>>> f = open(path, "a")
>>> f.write(content)
49
>>> f.write("\n")
1
>>> f.writelines(["black\n", "grey\n", "white\n"])
>>> f.close()
>>> 
