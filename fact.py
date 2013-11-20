#!/usr/bin/env python3
# max number to calculate 10
# max pool size = 8

import sys
from multiprocessing import Pool

def factorial(n):
	if n == 0:
		return 0
	elif n <= 1:
		return 1
	else:
		result = n * factorial(n - 1)
	return result

def printcalculation(n):
	list = []
	for n in range(1,n+1):
		str1 = str(n)
		str2 = "! = "
		list.insert(0, n)
		if n == 1:
			newstr = "".join((str1, str2, '1'))
		else:
			str3 = " * ".join(str(item) for item in list)
			newstr = "".join((str1, str2, str3, ' = ', str(factorial(n))))
	return newstr

if __name__ == '__main__':
	n = int(sys.argv[1])
	p = int(sys.argv[2])

	if n == 0:
		print("You shall not calculate the factorial of '0'")
	elif n > 10:
		print("You are not allowed to calculate the factorial of > 10")
	elif p == 0:
		print("Well... I can't really do my job without any workers, can I?")
	elif p > 10:
		print("You are not allowed to run this calculation with > 10 workers")
	else:
		pool = Pool(processes=p)	
		returnlist = pool.map(printcalculation, range(n, 0, -1))
		for item in reversed(returnlist):
			print(item)
