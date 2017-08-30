

filename = "pairs.txt"
hrange = [5]
#mrange = [0,10,20,30,40,50]
mrange = range(0,60)

with open(filename, "wb") as fout:
	for ampm in ["pm"]:
		for hours in hrange:
			for mins in mrange:
				timecase = ampm + ' '
				timecase += str(hours) + ':'
				timecase += str(mins)
				#print(timecase)
				fout.write(timecase + '\n')