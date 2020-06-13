import re

examples1 = {
	">": 2,
	"^>v<": 4,
	"^v^v^v^v^v": 2
}

examples2 = {
	"^v": 3,
	"^>v<": 3,
	"^v^v^v^v^v": 11
}

def day3a(test=False):
	if test:
		inputs = examples1
	else:
		inputs = open("d3.txt", "r").read().strip()
	prezzies = {}
	x = 0
	y = 0
	prezzies[(x, y)] = 1
	for item in inputs:
		if test:
			prezzies = {}
			x = 0
			y = 0
			prezzies[(x, y)] = 1
		for cha in item:
			if cha == "^":
				y += 1
			elif cha == "v":
				y -= 1
			elif cha == ">":
				x += 1
			elif cha == "<":
				x -= 1
			if (x, y) not in prezzies:
				prezzies[(x, y)] = 0
			prezzies[(x, y)] += 1
		if test:
			print(len(prezzies) == examples1[item])
	if not test:
		print(len(prezzies))


def day3b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = open("d3.txt", "r").read().strip()
	prezzies = {}
	xs = 0
	ys = 0
	xr = 0
	yr = 0
	prezzies[(xs, ys)] = 0
	which = "santa"
	for item in inputs:
		if test:
			prezzies = {}
			xs = 0
			ys = 0
			xr = 0
			yr = 0
			prezzies[(xs, ys)] = 1
		for cha in item:
			if which == "santa":
				if cha == "^":
					ys += 1
				elif cha == "v":
					ys -= 1
				elif cha == ">":
					xs += 1
				elif cha == "<":
					xs -= 1
				if (xs, ys) not in prezzies:
					prezzies[(xs, ys)] = 0
				prezzies[(xs, ys)] += 1
				which = "robot"
			elif which == "robot":
				if cha == "^":
					yr += 1
				elif cha == "v":
					yr -= 1
				elif cha == ">":
					xr += 1
				elif cha == "<":
					xr -= 1
				if (xr, yr) not in prezzies:
					prezzies[(xr, yr)] = 0
				prezzies[(xr, yr)] += 1
				which = "santa"
		if test:
			print(len(prezzies) == inputs[item])
	if not test:
		print(len(prezzies))

day3a()
day3b()
