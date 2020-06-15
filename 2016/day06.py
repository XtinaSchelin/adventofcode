example = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

answer = {
	"a": "easter",
	"b": "advent"
}

def do_day(test=False, day="a"):
	if test:
		inputs = example.split("\n")
	else:
		inputs = open("d6.txt", "r").read().split("\n")
	width = len(inputs[0])
	height = len(inputs)
	newb = {}
	for col in range(width):
		newb[col] = []
		for y in range(len(inputs)):
			newb[col].append(inputs[y][col])
	passcode = ""
	for col in range(width):
		if day == "a":
			passcode += max(set(newb[col]), key = newb[col].count)
		else:
			passcode += min(set(newb[col]), key = newb[col].count)
	print(passcode)
	if test:
		print(passcode == answer[day])

do_day(test=False, day="a")
do_day(test=False, day="b")
