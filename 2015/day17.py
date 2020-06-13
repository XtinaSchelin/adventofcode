import itertools

example = [20, 15, 10, 5, 5]
ex_total = 25
real_total = 150

def do_day(test=False, day="a"):
	if test:
		containers = example
		maximum = ex_total
	else:
		containers = [int(x) for x in open("d17.txt", "r").read().split("\n")]
		maximum = real_total
	solutions = 0
	minsols = {}
	for x in range(1, len(containers) + 1):
		for pairing in itertools.combinations(containers, x):
			tote = 0
			for itm in pairing:
				tote += itm
			if tote == maximum:
				if day == "a":
					solutions += 1
				else:
					if len(pairing) not in minsols:
						minsols[len(pairing)] = 0
					minsols[len(pairing)] += 1
	if day == "a":
		print(solutions)
	else:
		lowest = 99
		for item in minsols:
			if item < lowest:
				lowest = item
				solutions = minsols[item]
		print(solutions)

do_day(test=False, day="a")
do_day(test=False, day="b")
