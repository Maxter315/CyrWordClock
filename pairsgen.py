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

def addHours(hrs, mins, ampm):
	hours_list = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять","десять","одиннадцать","двенадцать"]
	hours_list_e = ["первого","второго","третьего","четвертого","пятого","шестого","седьмого","восьмого","девятого","десятого","одиннадцатого","двенадцатого"]
	out = ""
	daytime_list = ["утра","дня","вечера","ночи"]

	if mins in range(3,33):
		out += hours_list_e[hrs%12]
		out += " " * (15+7 - len(out)/2)
	else:
		if mins in range(0,3):
			out += hours_list[hrs]
		else:
			out += hours_list[hrs%12+1]

		out += " " * (15 - len(out)/2)

		if mins in range(0,3):
			if hrs == 1:
				out += "час    "
			elif hrs in [2,3,4]:
				out += "часa   "
			else:
				out += "часов  "
		else:
			if hrs == 12:
				out += "час    "
			elif hrs in [1,2,3]:
				out += "часa   "
			else:
				out += "часов  "

		if ampm == "am":
			if hrs in range(0,4) + [12]:
				out += daytime_list[3]
			
			if hrs in range(4,12):
				out += daytime_list[0]
		else:
			if hrs in range(0,6) + [12]:
				out += daytime_list[1]

			if hrs in range(6,12):
				out += daytime_list[2]

	return out

def addDay(hours, ampm):
	daytime_list = ["утра","дня","вечера","ночи"]

	if ampm == "am":
		if hours in range(0,4) + [12]:
			out = daytime_list[3]
		
		if hours in range(4,12):
			out = daytime_list[0]
	else:
		if hours in range(0,6) + [12]:
			out = daytime_list[1]

		if hours in range(6,12):
			out = daytime_list[2]

	out += " " * (8 - len(out)/2)

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
				words += addHours(hours, mins, ampm)
				#words += addDay(hours, ampm)


				fout.write(timecase + "\t" + words + '\n')

			fout.write("\n")
		
		fout.write("\n")
