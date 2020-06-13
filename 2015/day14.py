example = [
	"Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
	"Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]
ex_race = 1000

def do_day(test=False, racelen=0, day="a"):
	if test:
		inputs = example
	else:
		inputs = open("d14.txt", "r").read().split("\n")
	# Set the reindeer.
	reindeer = {}
	for rd in inputs:
		pieces = rd.split(" ")
		reindeer[pieces[0]] = {
			"speed": int(pieces[3]),
			"duration": int(pieces[6]),
			"rest": int(pieces[13]),
			"distance": 0,
			"scoring": 0,
			"chonks": []
		}
	for deer in reindeer:
		doe = []
		while len(doe) < racelen:
			for x in range(reindeer[deer]["duration"]):
				doe.append(reindeer[deer]["speed"])
			for x in range(reindeer[deer]["rest"]):
				doe.append(0)
		reindeer[deer]["chonks"] = doe
	for x in range(racelen):
		for deer in reindeer:
			reindeer[deer]["distance"] += reindeer[deer]["chonks"][x]
		if day == "b":
			maxdist = 0
			for deer in reindeer:
				if reindeer[deer]["distance"] > maxdist:
					maxdist = reindeer[deer]["distance"]
			for deer in reindeer:
				if reindeer[deer]["distance"] == maxdist:
					reindeer[deer]["scoring"] += 1
	if day == "a":
		maxdist = 0
		for deer in reindeer:
			if reindeer[deer]["distance"] > maxdist:
				maxdist = reindeer[deer]["distance"]
		print(maxdist)
	else:
		maxscore = 0
		for deer in reindeer:
			if reindeer[deer]["scoring"] > maxscore:
				maxscore = reindeer[deer]["scoring"]
		print(maxscore)

do_day(test=False, racelen=2503)
do_day(test=False, racelen=2503, day="b")
