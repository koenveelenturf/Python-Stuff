#!/usr/bin/env python3

import sys

print("Calculator: ")
print("1) Add")
print("2) Substract")
print("3) Multiply")
print("4) Divide")
print("q) Quit this program")

numbers = []
choice = None

def options(prompt, option=('1', '2', '3', '4', 'q')):
	while True:
		choice = input( prompt )
		if len(choice) < 1:
			return default
		elif choice in option:
			return choice

function = options("What do you want to do? Your choice: ")

if function == 'q':
	print("Exiting calculator... Bye!")
	sys.exit();

amount = int(input("How many numbers do you need? "))
answer = float(input("#1: "))

for i in range(amount-1):
	if function == '1':
		answer += float(input("#"+str(i+2)+": "))
	if function == '2':
		answer -= float(input("#"+str(i+2)+": "))
	if function == '3':
		answer *= float(input("#"+str(i+2)+": "))
	if function == '4':
		number = float(input("#"+str(i+2)+": "))
		while number == '0':
			print("You stupid old bad!")
			number = float(input("#"+str(i+2)+": "))
		else:
			answer /= cijfer

print("Result: ",answer)
