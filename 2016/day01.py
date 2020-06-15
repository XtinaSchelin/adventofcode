

examples1 = [
	["R2, L3", 5],
	["R2, R2, R2", 2],
	["R5, L5, R5, R3", 12]
]

examples2 = [
	["R8, R4, R4, R8", 4]
]

directions = ["N", "E", "S", "W"]

def do_day_a(test=False):
	if test:
		inputs = examples1
	else:
		inputs = [[open("d1.txt", "r").read()]]
	for paths in inputs:
		poz = "N"
		beg = [0, 0]
		steps = paths[0].split(", ")
		for step in steps:
			s_turn = step[0:1]
			s_dist = int(step[1:])
			if s_turn == "R":
				x = directions.index(poz) + 1
				if x >= len(directions):
					x = 0
			elif s_turn == "L":
				x = directions.index(poz) - 1
				if x < 0:
					x = 3
			poz = directions[x]
			if poz == "N":
				beg[1] += s_dist
			elif poz == "E":
				beg[0] += s_dist
			elif poz == "S":
				beg[1] -= s_dist
			elif poz == "W":
				beg[0] -= s_dist
		print("Distance:", abs(beg[0]) + abs(beg[1]))


def do_day_b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = [[open("d1.txt", "r").read()]]
	all_coords = []
	for paths in inputs:
		poz = "N"
		beg = [0, 0]
		steps = paths[0].split(", ")
		go = True
		for step in steps:
			if not go:
				break
			s_turn = step[0:1]
			s_dist = int(step[1:])
			if s_turn == "R":
				x = directions.index(poz) + 1
				if x >= len(directions):
					x = 0
			elif s_turn == "L":
				x = directions.index(poz) - 1
				if x < 0:
					x = 3
			poz = directions[x]
			if poz == "N":
				for q in range(s_dist):
					beg[1] += 1
					if str(beg) in all_coords:
						go = False
						break
					else:
						all_coords.append(str(beg))
			elif poz == "E":
				for q in range(s_dist):
					beg[0] += 1
					if str(beg) in all_coords:
						go = False
						break
					else:
						all_coords.append(str(beg))
			elif poz == "S":
				for q in range(s_dist):
					beg[1] -= 1
					if str(beg) in all_coords:
						go = False
						break
					else:
						all_coords.append(str(beg))
			elif poz == "W":
				for q in range(s_dist):
					beg[0] -= 1
					if str(beg) in all_coords:
						go = False
						break
					else:
						all_coords.append(str(beg))
		print("Distance:", abs(beg[0]) + abs(beg[1]))

do_day_a(test=False)
do_day_b(test=False)
