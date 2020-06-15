import sys

examples = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

def do_day(test=False, day="a"):
	if test:
		inputs = examples.split("\n")
	else:
		inputs = open("d12.txt", "r").read().split("\n")
	# Populate the register, apparently.
	register = {}
	for x in inputs:
		pieces = x.split(" ")
		if len(pieces) == 2:
			if pieces[1] not in register:
				register[pieces[1]] = 0
		elif pieces[0] == "cpy":
			if pieces[1] not in register:
				register[pieces[2]] = 0
	if day == "b":
		register["c"] = 1
	lenx = len(inputs)
	x = 0
	while x < lenx:
		pieces = inputs[x].split(" ")
		if pieces[0] == "cpy":
			try:
				register[pieces[2]] = int(pieces[1])
			except:
				register[pieces[2]] = register[pieces[1]]
			x += 1
		elif pieces[0] == "inc":
			register[pieces[1]] += 1
			x += 1
		elif pieces[0] == "dec":
			register[pieces[1]] -= 1
			x += 1
		elif pieces[0] == "jnz":
			try:
				if int(pieces[1]) != 0:
					x += int(pieces[2])
				else:
					x += 1
			except:
				if register[pieces[1]] != 0:
					x += int(pieces[2])
				else:
					x += 1
	print(register["a"])

do_day(test=False, day="a")
do_day(test=False, day="b")
