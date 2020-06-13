import sys
import re
import hashlib
import operator

txtfile = "d4.txt"

examples = [
	["abcdef", "609043"],
	["pqrstuv", "1048970"]
]

def do_day(test=False, l=0):
	if test:
		inputs = examples
	else:
		inputs = [open(txtfile, "r").read().strip().split("\n")]
	for imp in inputs:
		pmi = imp[0]
		x = 1
		while True:
			result = hashlib.md5((pmi + str(x)).encode("utf-8")).hexdigest()
			if l == 5:
				if result[0:5] == "00000":
					break
			elif l == 6:
				if result[0:6] == "000000":
					break
			x += 1
		print(l, "==", x)
		if test:
			print(x == int(imp[1]))

do_day(l=5)
do_day(l=6)
