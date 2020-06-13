import json
import re

examples1 = [
	['[1,2,3]', 6],
	['{"a":2,"b":4}', 6],
	['[[[3]]]', 3],
	['{"a":{"b":4},"c":-1}', 3],
	['{"a":[-1,1]}', 0],
	['[-1,{"a":1}]', 0],
	['[]', 0],
	['{}', 0],
]

def do_day(test=False):
	if test:
		inputs = examples1
	else:
		inputs = [open("d12.txt", "r").read()]
	for item in inputs:
		if not test:
			item = [item]
		meti = re.findall(r'[-?\d]+', item[0])
		summo = 0
		for itm in meti:
			summo += int(itm)
		print(summo)
		if test:
			print(summo == item[1])

do_day()
