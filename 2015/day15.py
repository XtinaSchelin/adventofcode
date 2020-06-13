import itertools
import re

def do_day(day="a"):
	inputs = open("d15.txt", "r").read().split("\n")
	ingredients = {}
	all_items = []
	patt = "^([^:]+): capacity ([^,]+), durability ([^,]+), flavor ([^,]+), texture ([^,]+), calories ([^,]+)$"
	for line in inputs:
		pieces = re.match(patt, line.strip()).groups()
		ingredients[pieces[0]] = {
			"capacity": int(pieces[1]),
			"durability": int(pieces[2]),
			"flavor": int(pieces[3]),
			"texture": int(pieces[4]),
			"calories": int(pieces[5])
		}
		all_items.append(pieces[0])
	max_total = 0
	amt_w = 0
	amt_x = 0
	amt_y = 0
	amt_z = 0
	amounts = {}
	for w in range(1, 101):
		for x in range(1, 101):
			for y in range(1, 101):
				for z in range(1, 101):
					if w + x + y + z == 100:
						amounts[all_items[0]] = w
						amounts[all_items[1]] = x
						amounts[all_items[2]] = y
						amounts[all_items[3]] = z
						total_cap = 0
						total_dur = 0
						total_flv = 0
						total_txt = 0
						total_cal = 0
						for item in all_items:
							total_cap += ingredients[item]["capacity"] * amounts[item]
							total_dur += ingredients[item]["durability"] * amounts[item]
							total_flv += ingredients[item]["flavor"] * amounts[item]
							total_txt += ingredients[item]["texture"] * amounts[item]
							total_cal += ingredients[item]["calories"] * amounts[item]
						if total_cap < 0: total_cap = 0
						if total_dur < 0: total_dur = 0
						if total_flv < 0: total_flv = 0
						if total_txt < 0: total_txt = 0
						if total_cal == 500 or day == "a":
							current_total = total_cap * total_dur * total_flv * total_txt
							if current_total > max_total:
								max_total = current_total
								amt_w = w
								amt_x = x
								amt_y = y
								amt_z = z
	print(day, max_total)

do_day(day="a")
do_day(day="b")
