Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # LAMBDA FUNCTIONS AND ITS USES
>>> 
>>> # lambda <inputexpr> : <outputeexpr>
>>> f = lambda a,b : a + b
>>> type(f)
<class 'function'>
>>> 
>>> f(10, 10)
20
>>> f("abd","def")
'abddef'
>>> f([1,2,4], [3,4,5])
[1, 2, 4, 3, 4, 5]
>>> 
>>> c2f = lambda t : t * 1.8 + 32
>>> c2f(100)
212.0
>>> 
>>> # --------------------------------------------------
>>> 
>>> T = [100, 13, 43, 56, 78, 99]
>>> F = []
>>> for t in T:
	f = t * 1.8 + 32
	F.append(f)

	
>>> F
[212.0, 55.400000000000006, 109.4, 132.8, 172.4, 210.20000000000002]
>>> 
>>> F1 = map(lambda t : t * 1.8 + 32, T)
>>> F1
<map object at 0x000001EFA8649C88>
>>> list(F1)
[212.0, 55.400000000000006, 109.4, 132.8, 172.4, 210.20000000000002]
>>> 
>>> 
>>> a = ["14,500", "45,788", "89,453"]
>>> A = map(lambda i : int(i.replace(',', '')), a)
>>> A
<map object at 0x000001EFA86456D8>
>>> list(A)
[14500, 45788, 89453]
>>> 
>>> # ---------------------------------- filter
>>> 
>>> import random
>>> R = []
>>> for i in range(100):
	R.append(random.randint(1, 100))

	
>>> R
[68, 51, 97, 53, 81, 63, 27, 27, 75, 49, 14, 31, 46, 68, 31, 99, 65, 58, 8, 45, 79, 71, 27, 68, 32, 39, 55, 82, 43, 13, 32, 68, 50, 94, 14, 5, 77, 78, 81, 100, 22, 56, 74, 53, 87, 3, 1, 91, 91, 83, 55, 30, 38, 17, 54, 41, 92, 91, 86, 50, 21, 31, 42, 1, 70, 65, 2, 66, 87, 58, 72, 69, 35, 57, 73, 78, 59, 5, 87, 82, 87, 4, 9, 16, 9, 51, 62, 49, 34, 61, 6, 74, 97, 93, 32, 51, 44, 69, 61, 48]
>>> 
>>> f = []
>>> for r in R:
	if(r % 3 == 0):
		f.append(r)

		
>>> f
[51, 81, 63, 27, 27, 75, 99, 45, 27, 39, 78, 81, 87, 3, 30, 54, 21, 42, 66, 87, 72, 69, 57, 78, 87, 87, 9, 9, 51, 6, 93, 51, 69, 48]
>>> 
>>> F = filter(lambda n : (n % 3 == 0), R)
>>> list(F)
[51, 81, 63, 27, 27, 75, 99, 45, 27, 39, 78, 81, 87, 3, 30, 54, 21, 42, 66, 87, 72, 69, 57, 78, 87, 87, 9, 9, 51, 6, 93, 51, 69, 48]
>>> 
>>> 
>>> # ------------------------------------------------ reduce
>>> 
>>> from functools import reduce
>>> 
>>> L = [1,2,3,4,5]
>>> reduce(lambda a,b:a+b, L)
15
>>> 
>>> # --------------------------------------- zip
>>> 
>>> T1 = ("anil", "sunil", "raj")
>>> T2 = ("bangalore", "hyderabad", "chennai")
>>> zip(T1, T2)
<zip object at 0x000001EFA86EA548>
>>> dict(zip(T1, T2))
{'anil': 'bangalore', 'sunil': 'hyderabad', 'raj': 'chennai'}
>>> 
>>> # ------------------------------------- sort
>>> 
>>> L = ["red", "blue", "orange", "golden", "cyan"]
>>> L.sort()
>>> L
['blue', 'cyan', 'golden', 'orange', 'red']
>>> L.sort(key=lambda i : i[-1])
>>> L
['red', 'blue', 'orange', 'cyan', 'golden']
>>> L.sort()
>>> L
['blue', 'cyan', 'golden', 'orange', 'red']
>>> L.sort(reverse=True)
>>> L
['red', 'orange', 'golden', 'cyan', 'blue']
>>> 
>>> 
>>> # -------------------------------------- unzipping
>>> 
>>> D = {'anil': 'bangalore', 'sunil': 'hyderabad', 'raj': 'chennai'}
>>> zip(*D.items())
<zip object at 0x000001EFA86EA548>
>>> list(zip(*D.items()))
[('anil', 'sunil', 'raj'), ('bangalore', 'hyderabad', 'chennai')]
>>> D.keys()
dict_keys(['anil', 'sunil', 'raj'])
>>> D.values()
dict_values(['bangalore', 'hyderabad', 'chennai'])
>>> 
>>> # --------------------------------------- comprehensions
>>> 
>>> n11 = [x for x in range(100, 201) if x % 11 == 0]
>>> n11
[110, 121, 132, 143, 154, 165, 176, 187, 198]
>>> 
>>> # <expr> <loop> <condition>
>>> 
>>> n5 = [x for x in range(100) if x % 5 == 0]
>>> n5
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> 
>>> nsq = ( (x, x**2) for x in range(1, 11) )
>>> nsq
<generator object <genexpr> at 0x000001EFA869B930>
>>> tuple(nsq)
((1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100))
>>> L
['red', 'orange', 'golden', 'cyan', 'blue']
>>> D = { s:len(s) for s in L }
>>> D
{'red': 3, 'orange': 6, 'golden': 6, 'cyan': 4, 'blue': 4}
>>> R = [random.randint(1, 100) for i in range(100)]
>>> R
[46, 98, 77, 2, 25, 100, 47, 8, 55, 13, 27, 56, 43, 1, 86, 80, 11, 15, 76, 14, 59, 13, 67, 66, 74, 40, 89, 16, 3, 15, 52, 81, 39, 100, 48, 53, 37, 87, 14, 85, 43, 34, 29, 90, 26, 85, 20, 27, 56, 57, 23, 49, 86, 59, 69, 19, 38, 43, 82, 63, 12, 58, 79, 78, 21, 93, 45, 91, 27, 88, 1, 27, 17, 50, 93, 28, 28, 53, 80, 19, 66, 73, 83, 35, 54, 14, 93, 2, 35, 8, 90, 10, 87, 100, 100, 44, 71, 83, 3, 99]
>>> 
>>> 
>>> L = list(range(1, 11))
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> 
>>> L2 =[x**2 for x in L]
>>> L2
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> L3 = [x/3 == 0 for x in L]
>>> L3
[False, False, False, False, False, False, False, False, False, False]
>>> L3 = [x**2 for x in L if x % 2 == 0]
>>> L3 = [x**2 for x in L if x % 3 == 0]
>>> L3
[9, 36, 81]
>>> 
>>> L4 = [x**2 if x % 3 == 0 else x for x in L]
>>> L4
[1, 2, 9, 4, 5, 36, 7, 8, 81, 10]
>>> 
