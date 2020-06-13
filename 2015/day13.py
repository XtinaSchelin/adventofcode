import itertools

example = """Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol."""

def do_day(test=False, day="a"):
	if test:
		inputs = example.split("\n")
	else:
		inputs = open("d13.txt", "r").read().split("\n")
	# Get the variables.
	people = []
	seatings = []
	for pair in inputs:
		pieces = pair[0:-1].split(" ")
		person1 = pieces[0]
		amount = int(pieces[3])
		if pieces[2] == "lose":
			amount *= -1
		person2 = pieces[10]
		if person1 not in people:
			people.append(person1)
		if person2 not in people:
			people.append(person2)
		seatings.append([person1, person2, amount])
	if day == "b":
		for person in people:
			seatings.append([person, "Self", 0])
			seatings.append(["Self", person, 0])
		people.append("Self")
	maxindex = 0
	for pairing in itertools.permutations(people):
		happindex = 0
		for x in range(len(people)):
			p1 = x
			p2 = x + 1
			if p2 == len(people):
				p2 = 0
			for seat in seatings:
				if pairing[p1] == seat[0] and pairing[p2] == seat[1]:
					happindex += seat[2]
				if pairing[p2] == seat[0] and pairing[p1] == seat[1]:
					happindex += seat[2]
			if happindex > maxindex:
				maxindex = happindex
	return maxindex

result_a = do_day(test=False)
print("A:", result_a)
result_b = do_day(test=False, day="b")
print("B:", result_b)
