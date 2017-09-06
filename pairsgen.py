# -*- coding: utf-8 -*-

def addEqual(minutes):
	exact_mins = [0,5,10,15,20,25,30,35,40,45,50,55]
	almost_mins = [8,13,18,23,27,28,33,38,43,48,53,57,58]
	out = ""

	if minutes in exact_mins:
		out += "ровно   "
	elif minutes in almost_mins:
		out += "  почти "
	else:
		out += "        "
	
	return out

def addWithout(minutes):
	out = ""

	if minutes > 32 and minutes < 57:
		out += "без   "
	else:
		out += "      "

	return out

def addMins(minutes):
	out = ""

	if minutes in [3,4]:
		out += "начало   "
	elif minutes in range(8,13):
		out += "десять   "
	elif minutes in range(13,18):
		out += "четверть "
	elif minutes in range(18,27):
		out += "двадцать "
	elif minutes in range(27,33):
		out += "половина "
	elif minutes in range(33,43):
		out += "двадцати "
	elif minutes in range(43,48):
		out += "четверти "
	elif minutes in range(48,53):
		out += "десяти   "
	else:
		out += "         "


	if minutes in [5,6,7,23,24,25,26]:
		out += "пять   "
	elif minutes in [33,34,35,36,37,53,54,55,56]:
		out += "пяти   "
	else:
		out += "       "


	if minutes in range(5,13) + range(18,27) + range(33,43) + range(18,27):
		out += "минут  "
	else:
		out += "       "

	return out







filename = "pairs4.txt"

hrange = [12,1,2,3,4,5,6,7,8,9,10,11]
#mrange = [0,10,20,30,40,50]
#mrange = range(0,60)
#mrange = ["00", "30"]
mrange = range(0,60)
hours_list = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать"]
hours_list_e = ["первого","второго","третьего","четвертого","пятого","шестого","седьмого","восьмого","девятого","десятого","одиннадцатого","двенадцатого"]



with open(filename, "wb") as fout:

	for ampm in ["am", "pm"]:

		for hours in hrange:

			for mins in mrange:

				timecase = ampm + ' '

				timecase += str(hours).zfill(2) + ':'
				timecase += str(mins).zfill(2)
				
				#if mins == "00":
				#	words = hours_list[hours] + " час/а/ов"
				#if mins == "30":
				#	words = "половина " + hours_list_e[hours]

				words = addEqual(mins)
				words += addWithout(mins)
				words += addMins(mins)


				fout.write(timecase + "\t" + words + '\n')

			fout.write("\n")
		
		fout.write("\n")
