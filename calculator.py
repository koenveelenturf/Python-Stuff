#!/usr/bin/env python3

import sys

print("Calculator: ")
print("1) Add")
print("2) Substract")
print("3) Multiply")
print("4) Divide")
print("q) Quit this program")

numbers = []
invoer=None

def option(prompt, option=('1', '2', '3', '4', 'q')):
	while True:
		invoer = input( prompt )
		if len(invoer) < 1:
			return default
		elif invoer in option:
			return invoer

keus = option("What do you want to do? Your choice: ")
cijfers = int(input("How many numbers do you need? "))
answer = float(input("#1: "))

if option == 'q':
	sys.exit(i);

for i in range(cijfers-1):
	if keus == '1':
		answer += float(input("#"+str(i+2)+": "))
	if keus == '2':
		answer -= float(input("#"+str(i+2)+": "))
	if keus == '3':
		answer *= float(input("#"+str(i+2)+": "))
	if keus == '4':
		cijfer = float(input("#"+str(i+2)+": "))
		while cijfer == '0':
			print("You stupid old bad!")
			cijfer = float(input("#"+str(i+2)+": "))
		else:
			answer /= cijfer

print("Result: ",answer)
