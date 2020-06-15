import re
import hashlib

salt = "abc"
indects = 0

def check_hash(imp, ecks):
	temp = hashlib.md5((imp + str(ecks)).encode("utf-8"))
	trip = re.search(r"(.)\1\1", temp.hexdigest())
	found = False
	if trip is not None:
		findio = trip.group(1) * 5
		for x in range(1, 1001):
			pmet = hashlib.md5((imp + str(x + int(ecks))).encode("utf-8"))
			pirt = pmet.hexdigest().find(findio)
			if pirt > -1:
				found = True
				break
	if found:
		return temp.hexdigest()
	return ""

all_keys = []
while True:
	key = check_hash(salt, str(indects))
	if key != "":
		all_keys.append(key)
	if len(all_keys) == 64:
		break
	indects += 1

print(indects)
