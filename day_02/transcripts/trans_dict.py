Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L = ["Anil", 35, "HPE", "Bangalore"]
>>> L[0]
'Anil'
>>> L[2]
'HPE'
>>> 
>>> D = { "name":"Anil", "age":35, "company":"HPE", "place":"Bangalore"}
>>> type(D)
<class 'dict'>
>>> 
>>> D['name']
'Anil'
>>> D['company']
'HPE'
>>> 
>>> # ---------------------- Add, remove, modify
>>> 
>>> D['name'] = "Anil Kumar"
>>> D
{'name': 'Anil Kumar', 'age': 35, 'company': 'HPE', 'place': 'Bangalore'}
>>> D['salary']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    D['salary']
KeyError: 'salary'
>>> D['salary'] = "1000000 INR"
>>> D
{'name': 'Anil Kumar', 'age': 35, 'company': 'HPE', 'place': 'Bangalore', 'salary': '1000000 INR'}
>>> 
>>> D1 = {"addr":"Whitefield", "hobbies":['cricket', 'music']}
>>> D
{'name': 'Anil Kumar', 'age': 35, 'company': 'HPE', 'place': 'Bangalore', 'salary': '1000000 INR'}
>>> D.update(D1)
>>> D
{'name': 'Anil Kumar', 'age': 35, 'company': 'HPE', 'place': 'Bangalore', 'salary': '1000000 INR', 'addr': 'Whitefield', 'hobbies': ['cricket', 'music']}
>>> 
>>> D.pop('addr')
'Whitefield'
>>> D
{'name': 'Anil Kumar', 'age': 35, 'company': 'HPE', 'place': 'Bangalore', 'salary': '1000000 INR', 'hobbies': ['cricket', 'music']}
>>> 
>>> 
>>> # ----------------------------------- important functions
>>> 
>>> D.keys()
dict_keys(['name', 'age', 'company', 'place', 'salary', 'hobbies'])
>>> D.values()
dict_values(['Anil Kumar', 35, 'HPE', 'Bangalore', '1000000 INR', ['cricket', 'music']])
>>> D.items()
dict_items([('name', 'Anil Kumar'), ('age', 35), ('company', 'HPE'), ('place', 'Bangalore'), ('salary', '1000000 INR'), ('hobbies', ['cricket', 'music'])])
>>> 
>>> 
>>> # --------------------------------
>>> 
>>> #  name   age   gender
>>> #  anil   35    M
>>> #  geetha 23    F
>>> 
>>> DA = {"name":"anil", "age":35, "gen":"M"}
>>> DG = {"name":"geetha", "age":23, "gen": "F"}
>>> da
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    da
NameError: name 'da' is not defined
>>> DA
{'name': 'anil', 'age': 35, 'gen': 'M'}
>>> DG
{'name': 'geetha', 'age': 23, 'gen': 'F'}
>>> ED = {DA, DG}
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ED = {DA, DG}
TypeError: unhashable type: 'dict'
>>> ED = {'anil':DA, 'geetha':DG}
>>> ED
{'anil': {'name': 'anil', 'age': 35, 'gen': 'M'}, 'geetha': {'name': 'geetha', 'age': 23, 'gen': 'F'}}
>>> ED.keys()
dict_keys(['anil', 'geetha'])
>>> ED['geetha']['age']
23
>>> ED['anil']['gen']
'M'
>>> 
>>> # ------------------- some experiments
>>> 
>>> ED.keys()
dict_keys(['anil', 'geetha'])
>>> for emp in ED.keys():
	print(emp)

	
anil
geetha
>>> for emp in ED.keys():
	print(ED[emp])

	
{'name': 'anil', 'age': 35, 'gen': 'M'}
{'name': 'geetha', 'age': 23, 'gen': 'F'}
>>> 
>>> 
>>> for emp in ED.keys():
	keys = ['name', 'age', 'gen']
	for key in keys:
		print(ED[emp][key], end='-')

		
anil-35-M-geetha-23-F-
>>> for emp in ED.keys():
	keys = ['name', 'age', 'gen']
	for key in keys:
		print(ED[emp][key], end='-')
	print('\n')

	
anil-35-M-

geetha-23-F-

>>> for emp in ED.keys():
	keys = ['name', 'age', 'gen']
	for key in keys:
		print(str(ED[emp][key]).ljust(20), end='|')
	print('\n')

	
anil                |35                  |M                   |

geetha              |23                  |F                   |

>>> 
