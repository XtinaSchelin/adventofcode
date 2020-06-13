import re

txtfile = "d6.txt"

example1 = [
	"turn on 0,0 through 999,999",
	"toggle 0,0 through 999,0",
	"turn off 499,499 through 500,500"
]
answer = 998996

example2 = [
	"turn on 0,0 through 0,0",
	"toggle 0,0 through 999,999"
]
answer = 2000001

def day_a(test=False):
	if test:
		inputs = example
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	lights = {}
	for x in range(0, 1000):
		for y in range(0, 1000):
			lights[(x, y)] = False
	patt = "^([^0-9]+) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$"
	for imp in inputs:
		act, x1, y1, x2, y2 = re.match(patt, imp).groups()
		for x in range(int(x1), int(x2) + 1):
			for y in range(int(y1), int(y2) + 1):
				if act == "turn off":
					lights[(x, y)] = False
				elif act == "turn on":
					lights[(x, y)] = True
				else:
					if lights[(x, y)]:
						lights[(x, y)] = False
					else:
						lights[(x, y)] = True
	lit = 0
	for x in range(0, 1000):
		for y in range(0, 1000):
			if lights[(x, y)]:
				lit += 1
	print(lit)
	if test:
		print(lit == answer)



def day_b(test=False):
	if test:
		inputs = example2
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	lights = {}
	for x in range(0, 1000):
		for y in range(0, 1000):
			lights[(x, y)] = 0
	patt = "^([^0-9]+) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$"
	for imp in inputs:
		act, x1, y1, x2, y2 = re.match(patt, imp).groups()
		for x in range(int(x1), int(x2) + 1):
			for y in range(int(y1), int(y2) + 1):
				if act == "turn off":
					lights[(x, y)] -= 1
					if lights[(x, y)] < 0:
						lights[(x, y)] = 0
				elif act == "turn on":
					lights[(x, y)] += 1
				else:
					lights[(x, y)] += 2
	lit = 0
	for x in range(0, 1000):
		for y in range(0, 1000):
			lit += lights[(x, y)]
	print(lit)
	if test:
		print(lit == answer)

day_a()
day_b()
