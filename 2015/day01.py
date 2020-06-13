import re

examples1 = [
	["(())", 0],
	["()()", 0],
	["(((", 3],
	["(()(()(", 3],
	["))(((((", 3],
	["())", -1],
	["))(", -1],
	[")))", -3],
	[")())())", -3]
]

examples2 = [
	[")", 1],
	["()()(", 5]
]

def day1a(test=False):
	if test:
		inputs = examples1
	else:
		inputs = [[open("d1.txt", "r").read().strip()]]
	for imp in inputs:
		rez = 0
		poz = 0

		for cha in imp[0]:
			rez += 1 if cha == "(" else -1
			poz += 1
		if test:
			print(rez == imp[1])
		else:
			print(rez)

def day1b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = [[open("d1.txt", "r").read().strip()]]
	for imp in inputs:
		rez = 0
		poz = 0
		for cha in imp[0]:
			rez += 1 if cha == "(" else -1
			poz += 1
			if rez < 0:
				break
		if test:
			print(poz == imp[1])
		else:
			print(poz)

day1a()
day1b()
