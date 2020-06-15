import re
from collections import Counter

txtfile = "d4.txt"

examples1 = [
	"aaaaa-bbb-z-y-x-123[abxyz]",
	"a-b-c-d-e-f-g-h-987[abcde]",
	"not-a-real-room-404[oarel]",
	"totally-real-room-200[decoy]"
]

examples2 = ["qzmt-zixmtkozy-ivhz-343"]

def day_a(test=False):
	if test:
		inputs = examples1
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	patt = "^([^0-9]+)([0-9]+)\[(.....)\]$"
	allnums = 0
	for imp in inputs:
		encname, sector, checksum = re.match(patt, imp).groups()
		sector = int(sector)
		encname = encname.replace("-", "")
		listio = []
		for item in Counter(encname).most_common():
			thisio = [item[1], item[0]]
			listio.append(thisio)
		collio = sorted(listio, key=lambda x: (-x[0], x[1]))
		stree = ""
		for x in range(0, 5):
			stree += collio[x][1]
		if stree == checksum:
			allnums += sector
	print(allnums)



def day_b(test=False):
	if test:
		inputs = examples2
	else:
		inputs = open(txtfile, "r").read().strip().split("\n")
	patt = "^(.+)-([0-9]+)\[.....\]$"
	offset = 96
	for imp in inputs:
		room, sector = re.match(patt, imp).groups()
		new = ""
		for ltr in room:
			if ltr == "-":
				new += " "
			else:
				new_ord = ord(ltr) - offset + int(sector)
				new_chr = new_ord % 26
				new += chr(new_chr + offset)
		if new.find("north") > -1:
			print(sector)


day_a()
day_b()
