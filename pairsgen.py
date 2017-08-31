# -*- coding: utf-8 -*-

filename = "pairs.txt"

hrange = range(0,12)
#mrange = [0,10,20,30,40,50]
#mrange = range(0,60)
mrange = ["00", "30"]
hours_list = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать"]
hours_list_e = ["первого","второго","третьего","четвертого","пятого","шестого","седьмого","восьмого","девятого","десятого","одиннадцатого","двенадцатого"]


with open(filename, "wb") as fout:

	for ampm in ["am", "pm"]:

		for hours in hrange:

			for mins in mrange:

				timecase = ampm + ' '
				timecase += str(hours).zfill(2) + ':'
				timecase += mins
				
				if mins == "00":
					words = hours_list[hours] + " час/а/ов"
				if mins == "30":
					words = "половина " + hours_list_e[hours]
				
				fout.write(timecase + "\t" + words + '\n')

		fout.write("\n")
