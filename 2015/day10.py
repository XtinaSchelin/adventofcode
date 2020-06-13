import re

def do_finding(stree):
	chonks = re.findall(r'((\w)\2{0,})', stree)

	newline = ""
	for chonk in chonks:
		newline += str(len(chonk[0])) + chonk[1]
	return newline

def do_day(l=0):
	inputs = open("d10.txt", "r").read()
	for x in range(l):
		inputs = do_finding(inputs)
	return len(inputs)

print(do_day(40))
print(do_day(50))
