import re

example = ".^^.^.^^^^"
rows = 10

def do_day(test=False, day="a"):
	if test:
		inputs = example
		rows = 10
	else:
		inputs = open("d18.txt", "r").read()
		if day == "a":
			rows = 40
		else:
			rows = 400000

	newrow = ""

	traps = [
		"tts",
		"stt",
		"tss",
		"sst"
	]

	total_map = [inputs]
	for q in range(rows - 1):
		newrow = ""
		for c in range(len(inputs)):
			ct = ""
			if c == 0 or inputs[c-1:c] == ".":
				ct += "s"
			elif inputs[c-1:c] == "^":
				ct += "t"
			if c == len(inputs) or inputs[c:c+1] == ".":
				ct += "s"
			elif inputs[c:c+1] == "^":
				ct += "t"
			if c + 1 == len(inputs) or inputs[c+1:c+2] == ".":
				ct += "s"
			elif inputs[c+1:c+2] == "^":
				ct += "t"

			if ct in traps:
				newrow += "^"
			else:
				newrow += "."
		total_map.append(newrow)
		inputs = newrow
	safe = 0
	for row in total_map:
		safe += len(re.findall(r"\.", row))
	print(safe)

do_day(False, day="a")
do_day(False, day="b")
