import re

examples1 = {
	"2x3x4": 58,
	"1x1x10": 43
}

examples2 = {
	"2x3x4": 34,
	"1x1x10": 14
}

def day2a(test=False):
	if test:
		inputs = examples
	else:
		inputs = open("d2.txt", "r").read().strip().split("\n")
	real_total = 0
	for item in inputs:
		wayall = 0
		bl, bw, bh = re.match("^([0-9]+)x([0-9]+)x([0-9]+)$", item).groups()
		bl = int(bl)
		bw = int(bw)
		bh = int(bh)
		ar1 = 2 * bl * bw
		ar2 = 2 * bw * bh
		ar3 = 2 * bh * bl
		total = ar1 + ar2 + ar3
		litems = sorted([bl, bw, bh], reverse=True)
		sm1 = litems.pop()
		sm2 = litems.pop()
		total += (sm1 * sm2)
		wayall += total
		if test:
			print(wayall)
			print(wayall == examples1[item])
		else:
			real_total += wayall
	if not test:
		print(real_total)


def day2b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = open("d2.txt", "r").read().strip().split("\n")
	real_total = 0
	for item in inputs:
		wayall = 0
		bl, bw, bh = re.match("^([0-9]+)x([0-9]+)x([0-9]+)$", item).groups()
		bl = int(bl)
		bw = int(bw)
		bh = int(bh)
		bow = bl * bw * bh
		litems = sorted([bl, bw, bh], reverse=True)
		sm1 = litems.pop() * 2
		sm2 = litems.pop() * 2
		wayall += bow + sm1 + sm2
		if test:
			print(wayall)
			print(wayall == examples2[item])
		else:
			real_total += wayall
	if not test:
		print(real_total)


day2a()
day2b()
