import sys
import re
import itertools

examples = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

def do_day(test=False, which="min"):
	if not test:
		distances = open("d9.txt").read().split("\n")
	else:
		distances = examples.split("\n")
	all_cities = []
	all_legs = []

	for dist in distances:
		pieces = dist.split(" ")
		city1 = pieces[0]
		city2 = pieces[2]
		leg = int(pieces[4])
		if city1 not in all_cities:
			all_cities.append(city1)
		if city2 not in all_cities:
			all_cities.append(city2)
		this_deal = [city1, city2, leg]
		all_legs.append(this_deal)

	most = 0 if which == "max" else 9999999
	trip = []

	for item in itertools.permutations(all_cities, len(all_cities)):
		dooth = 0
		chunks = {}
		for x in range(len(all_cities) - 1):
			chunks[x] = [item[x], item[x + 1]]
		total = 0
		for leg in all_legs:
			for x in range(len(all_cities) - 1):
				if leg[0] in chunks[x] and leg[1] in chunks[x]:
					total += leg[2]
					dooth += 1
		if which == "max":
			if total > most and dooth == len(all_cities) - 1:
				most = total
				trip = item
		else:
			if total < most and dooth == len(all_cities) - 1:
				most = total
				trip = item
	print(which, most)

do_day(which="min")
do_day(which="max")
