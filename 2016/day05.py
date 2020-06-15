import hashlib

example = {
	"a": ["abc", "18f47a30"],
	"b": ["abc", "05ace8e3"]
}

def find_hex(txt, num, day, l=5):
	m = hashlib.md5((txt + str(num)).encode("utf-8"))
	if m.hexdigest()[0:l] == "0" * l:
		if day == "a":
			return m.hexdigest()[5:6]
		else:
			if m.hexdigest()[5:6] in ["0", "1", "2", "3", "4", "5", "6", "7"]:
				return int(m.hexdigest()[5:6]), m.hexdigest()[6:7]
	if day == "a":
		return "Q"
	else:
		return "Q", "Q"


def do_day(test=False, day="a"):
	if test:
		inputs = example[day]
	else:
		inputs = [open("d5.txt", "r").read()]
	current = 0
	position = ""
	passcode = [".", ".", ".", ".", ".", ".", ".", "."]
	if day == "a":
		for x in range(8):
			while True:
				result = find_hex(inputs[0], current, day)
				if result[0] == "Q":
					current += 1
				else:
					current += 1
					passcode[x] = str(result)
					break
	else:
		while True:
			position, result = find_hex(inputs[0], current, day)
			if result[0] == "Q":
				current += 1
			else:
				current += 1
				print(position)
				if passcode[int(position)] == ".":
					passcode[int(position)] = str(result)
			if "." not in passcode:
				break

	print("".join(passcode))
	if test:
		print("".join(passcode) == inputs[1])

do_day(test=False, day="a")
do_day(test=False, day="b")
