import re

example_boss = """Hit Points: 12
Damage: 7
Armor: 2"""

example_self = """Hit Points: 8
Damage: 5
Armor: 5"""

weapons = {
	"dagger": {"Au": 8, "Dm": 4},
	"shortsword": {"Au": 10, "Dm": 5},
	"warhammer": {"Au": 25, "Dm": 6},
	"longsword": {"Au": 40, "Dm": 7},
	"greataxe": {"Au": 74, "Dm": 8}
}
armor = {
	"leather": {"Au": 13, "AC": 1},
	"chainmail": {"Au": 31, "AC": 2},
	"splintmail": {"Au": 53, "AC": 3},
	"bandedmail": {"Au": 75, "AC": 4},
	"platemail": {"Au": 102, "AC": 5},
	"[none]": {"Au": 0, "AC": 0}
}
rings = {
	"damage +1": {"Au": 25, "AC": 0, "Dm": 1},
	"damage +2": {"Au": 50, "AC": 0, "Dm": 2},
	"damage +3": {"Au": 100, "AC": 0, "Dm": 3},
	"defense +1": {"Au": 20, "AC": 1, "Dm": 0},
	"defense +2": {"Au": 40, "AC": 2, "Dm": 0},
	"defense +3": {"Au": 80, "AC": 3, "Dm": 0},
	"[none]": {"Au": 0, "AC": 0, "Dm": 0}
}

combos = []

for w in weapons:
	for a in armor:
		for r1 in rings:
			for r2 in rings:
				if r1 != r2 or (r1 == "[none]" and r2 == "[none]"):
					this_combo = {
						"weapon": w,
						"armor": a,
						"ring1": r1,
						"ring2": r2,
						"t_Au": weapons[w]["Au"] + armor[a]["Au"] + rings[r1]["Au"] + rings[r2]["Au"],
						"t_AC": armor[a]["AC"] + rings[r1]["AC"] + rings[r2]["AC"],
						"t_Dm": weapons[w]["Dm"] + rings[r1]["Dm"] + rings[r2]["Dm"]
					}
					combos.append(this_combo)

#for combo in combos:
#	print(combo)

def fight(boss, pc, Au, day):
	while True:
		# PC
		damage = pc["Dm"] - boss["AC"]
		if damage < 1: damage = 1
		boss["HP"] -= damage
		if boss["HP"] <= 0:
			break
		# Boss
		damage = boss["Dm"] - pc["AC"]
		if damage < 1: damage = 1
		pc["HP"] -= damage
		if pc["HP"] <= 0:
			break
	if day == "a":
		if boss["HP"] <= 0:
			return Au
		else:
			return -1
	else:
		if pc["HP"] <= 0:
			return Au
		else:
			return -1

def setup(bi, pi):
	temp = pi.split("\n")
	pc = {
		"HP": int(temp[0].split(" ")[2]),
		"Dm": int(temp[1].split(" ")[1]),
		"AC": int(temp[2].split(" ")[1]),
		"AU": 0
	}
	temp = bi.split("\n")
	boss = {
		"HP": int(temp[0].split(" ")[2]),
		"Dm": int(temp[1].split(" ")[1]),
		"AC": int(temp[2].split(" ")[1])
	}
	return boss, pc


def do_day(test=False, day="a"):
	if test:
		boss_input = example_boss
		pc_input = example_self
	else:
		boss_input = open("d21.txt", "r").read()
		pc_input = """Hit Points: 100
Damage: 0
Armor: 0"""
	boss, pc = setup(boss_input, pc_input)
	if test:
		Au = fight(boss, pc)
		print(Au)
	else:
		min_gold = 9999
		max_gold = 0
		for combo in combos:
			boss, pc = setup(boss_input, pc_input)
			pc["Dm"] = combo["t_Dm"]
			pc["AC"] = combo["t_AC"]
			pc["Au"] = combo["t_Au"]
			Au = fight(boss, pc, pc["Au"], day)
			if Au > -1:
				if day == "a" and Au < min_gold:
					min_gold = Au
				elif day == "b" and Au > max_gold:
					max_gold = Au
		if day == "a":
			print(min_gold)
		else:
			print(max_gold)

do_day(test=False, day="a")
do_day(test=False, day="b")
