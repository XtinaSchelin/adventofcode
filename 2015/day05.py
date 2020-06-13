import re

txtfile = "d5.txt"

examples1 = [
	["ugknbfddgicrmopn", True],
	["aaa", True],
	["jchzalrnumimnmhp", False],
	["haegwjzuvuyypxyu", False],
	["dvszwmarrgswjxmb", False]
]
examples2 = [
	["qjhvhtzxzqqjkmpb", True],
	["xxyxx", True],
	["uurcxstgmygtbstg", False],
	["ieodomkazucvgmuy", False],
	["aaa", False]
]

def day_a(test=False):
	if test:
		inputs = examples1
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	nice = 0
	for imp in inputs:
		if not test:
			imp = [imp]
		status = True
		if len(re.findall("[aeiou]", imp[0])) < 3:
			status = False
		if status and re.findall("(.)\\1", imp[0]) == []:
			status = False
		if status and re.findall("(ab|cd|pq|xy)", imp[0]) != []:
			status = False
		if status:
			nice += 1
		if test:
			print(status == imp[1])
	if not test:
		print("A:", nice)


def day_b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	nice = 0
	neat = 0
	for imp in inputs:
		if not test:
			imp = [imp]
		status = False
		if re.match("^.*(.).\\1.*$", imp[0]) is not None:
			status = True
		if status:
			status = False
			if re.match("^.*(..).*\\1.*$", imp[0]) is not None:
				status = True
		if status:
			nice += 1
		if test:
			print(status == imp[1])
	if not test:
		print("B:", nice)


day_a()
day_b()
