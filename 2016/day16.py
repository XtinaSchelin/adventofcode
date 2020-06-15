import re

def do_day(day="a"):
	if day == "a":
		maxlen = 272
	else:
		maxlen = 35651584

	a = "10111100110001111"

	while len(a) < maxlen:
		b = ""
		for x in range(len(a), -1, -1):
			l = a[x:x+1]
			if l != "":
				b += "0" if l == "1" else "1"
		a = a + "0" + b

	a = a[0:maxlen]

	def chex(string):
		pieces = re.findall("(..)", string)
		result = ""
		for p in pieces:
			if p[0:1] == p[1:]:
				result += "1"
			else:
				result += "0"
		if len(result) % 2 == 0:
			result = chex(result)
		return result

	print(chex(a))

do_day("a")
do_day("b")
