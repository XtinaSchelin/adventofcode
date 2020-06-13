import re
knowns = {
	"children": 3,
	"cats": 7,
	"samoyeds": 2,
	"pomeranians": 3,
	"akitas": 0,
	"vizslas": 0,
	"goldfish": 5,
	"trees": 3,
	"cars": 2,
	"perfumes": 1
}

greaters = ["cats", "trees"]
lessers = ["pomeranians", "goldfish"]

def do_day(day="a"):
	inputs = open("d16.txt", "r").read().split("\n")
	all_sues = {}
	patt = "^Sue ([0-9]+): ([^:]+): ([0-9]+), ([^:]+): ([0-9]+), ([^:]+): ([0-9]+)$"
	possibles = []
	for imp in inputs:
		pieces = re.match(patt, imp).groups()
		all_sues[pieces[0]] = {
			pieces[1]: int(pieces[2]),
			pieces[3]: int(pieces[4]),
			pieces[5]: int(pieces[6])
		}
		if day == "a":
			if knowns[pieces[1]] == int(pieces[2]) and knowns[pieces[3]] == int(pieces[4]) and knowns[pieces[5]] == int(pieces[6]):
				print(pieces[0])
		else:
			appendify = 0
			for x in range(1, 7, 2):
				if pieces[x] in greaters:
					if int(pieces[x + 1]) > knowns[pieces[x]]:
						appendify += 1
				elif pieces[x] in lessers:
					if int(pieces[x + 1]) < knowns[pieces[x]]:
						appendify += 1
				else:
					if int(pieces[x + 1]) == knowns[pieces[x]]:
						appendify += 1
			if appendify == 3:
				print(pieces[0])

do_day(day="a")
do_day(day="b")
