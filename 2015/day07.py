import re
import sys

varz = {}

def do_not(itm):
	bval = str(bin(varz[itm]))[2:]
	pilf = ""
	while len(bval) < 16:
		bval = "0" + bval
	for x in bval:
		if x == "1":
			pilf += "0"
		else:
			pilf += "1"
	return int(pilf, 2)

def do_andor(bv1, bv2, cmd):
	if bv1 == "1":
		bval1 = str(bin(1))[2:]
	else:
		bval1 = str(bin(varz[bv1]))[2:]
	bval2 = str(bin(varz[bv2]))[2:]
	while len(bval1) < 16:
		bval1 = "0" + bval1
	while len(bval2) < 16:
		bval2 = "0" + bval2
	new_bin = ""
	if cmd == "AND":
		for x in range(16):
			if bval1[x] == bval2[x]:
				new_bin += bval1[x]
			else:
				new_bin += "0"
	elif cmd == "OR":
		for x in range(16):
			if bval1[x] == "1" or bval2[x] == "1":
				new_bin += "1"
			else:
				new_bin += "0"
	while new_bin[0:1] == "0":
		new_bin = new_bin[1:]
	if len(new_bin) == 0:
		return 0
	return int(new_bin, 2)

# fix this one
def do_shift(bv, cmd, dist):
	bval = str(bin(varz[bv]))[2:]
	dist = int(dist)
	while len(bval) < 16:
		bval = "0" + bval
	if cmd == "LSHIFT":
		bval = bval[dist:] + ("0" * dist)
	else:
		bval = ("0" * int(dist)) + bval[0:(-1 * dist)]
	while bval[0:1] == "0":
		bval = bval[1:]
	if len(bval) == 0:
		return 0
	return int(bval, 2)

def do_lines(linez, whomst, repl):
	leftovers = []
	for line in linez:
		if line != "":
			which = ""
			pieces = line.split(" ")
			if pieces[1] in ["AND", "OR"]:
				if pieces[2] not in varz:
					leftovers.append(line)
				else:
					if pieces[0] == "1" or pieces[0] in varz:
						varz[pieces[4]] = do_andor(pieces[0], pieces[2], pieces[1])
					else:
						leftovers.append(line)
			elif pieces[1] in ["LSHIFT", "RSHIFT"]:
				if pieces[0] not in varz:
					leftovers.append(line)
				else:
					varz[pieces[4]] = do_shift(pieces[0], pieces[1], pieces[2])
			elif pieces[0] == "NOT":
				if pieces[1] not in varz:
					leftovers.append(line)
				else:
					varz[pieces[3]] = do_not(pieces[1])
			else:
				if whomst == "b" and pieces[2] == "b":
					varz["b"] = int(repl)
				else:
					try:
						varz[pieces[2]] = int(pieces[0])
					except:
						if pieces[0] not in varz:
							leftovers.append(line)
						else:
							varz[pieces[2]] = int(varz[pieces[0]])
	return leftovers

def do_day(test=False, which="a", repl=0):
	linez = open("d7.txt", "r").read().split("\n")
	lefts = linez
	while True:
		lefts = do_lines(lefts, which, repl)
		if lefts == []:
			break
	print(which, varz["a"])
	if which == "a":
		return varz["a"]
	return 0

varz = {}
var_a = do_day()
varz = {}
do_day(which="b", repl=var_a)
