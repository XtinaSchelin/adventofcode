import re

txtfile = "d2.txt"

examples = ["ULL", "RRDDD", "LURDL", "UUUUD"]

def day_a(test=False):
	if test:
		inputs = examples
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	numbers = [
		[1,2,3],
		[4,5,6],
		[7,8,9]
	]
	passcode = ""
	start = [1, 1]
	for dire in inputs:
		for erid in dire:
			if erid == "U":
				start[0] -= 1
				if start[0] < 0:
					start[0] = 0
			elif erid == "D":
				start[0] += 1
				if start[0] > 2:
					start[0] = 2
			elif erid == "L":
				start[1] -= 1
				if start[1] < 0:
					start[1] = 0
			elif erid == "R":
				start[1] += 1
				if start[1] > 2:
					start[1] = 2
		passcode += str(numbers[start[0]][start[1]])
	print(passcode)

def day_b(test=False):
	if test:
		inputs = examples
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	numbers = [
		['.','.','1','.','.'],
		['.','2','3','4','.'],
		['5','6','7','8','9'],
		['.','A','B','C','.'],
		['.','.','D','.','.']
	]
	start = [2, 0]
	passcode = ""
	for dire in inputs:
		for erid in dire:
			if erid == "U":
				start[0] -= 1
				if start[0] < 0 or numbers[start[0]][start[1]] == ".":
					start[0] += 1
			elif erid == "D":
				start[0] += 1
				if start[0] > 4 or numbers[start[0]][start[1]] == ".":
					start[0] -= 1
			elif erid == "L":
				start[1] -= 1
				if start[1] < 0 or numbers[start[0]][start[1]] == ".":
					start[1] += 1
			elif erid == "R":
				start[1] += 1
				if start[1] > 4 or numbers[start[0]][start[1]] == ".":
					start[1] -= 1
		passcode += str(numbers[start[0]][start[1]])
	print(passcode)


day_a(False)
day_b(False)
