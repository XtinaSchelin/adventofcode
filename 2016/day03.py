import operator
from pprint import pprint
import re

txtfile = "d3.txt"

patt = "^ *([0-9]+) *([0-9]+) *([0-9]+) *$"

examples = ["  5  10   15"]

def day_a(test=False):
	if test:
		inputs = examples
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	winning = 0
	for tryangle in inputs:
		sides = re.match(patt, tryangle)
		better = []
		for item in sides.groups():
			better.append(int(item))
		if better[0] + better[1] > better[2] and better[0] + better[2] > better[1] and better[1] + better[2] > better[0]:
			winning += 1
	print(winning)

def day_b(test=False):
	if test:
		inputs = examples
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	chonk = []
	all_chonks = []
	for x in range(0, len(inputs)):
		sides = re.match(patt, inputs[x])
		better = []
		for item in sides.groups():
			better.append(int(item))
		chonk.append(better)
		if operator.mod(x + 1, 3) == 0:
			all_chonks.append(chonk)
			chonk = []
	change = []
	for chonk in all_chonks:
		some = [[],[],[]]
		for knock in chonk:
			some[0].append(knock[0])
			some[1].append(knock[1])
			some[2].append(knock[2])
		change.append(some)
	winning = 0
	for item in change:
		for better in item:
			if better[0] + better[1] > better[2] and better[0] + better[2] > better[1] and better[1] + better[2] > better[0]:
				winning += 1
	print(winning)


day_a(False)
day_b(False)
