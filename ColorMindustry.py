import random
import os
import json
import re

__namelib__ = "ColorMindustry"
__version__ = "0.2-beta"
__author__ = "Roman Slabicky"
__company__ = "RCR"

class fw:
	colors = ["[black]", "[white]", "[lightgray]", "[gray]", "[darkgray]", "[blue]", "[navy]", "[royal]", "[slate]", "[sky]", "[cyan]", "[teal]", "[green]", "[charteuse]", "[lime]", "[forest]", "[olive]", "[yellow]", "[gold]", "[goldenrod]", "[orange]", "[brown]", "[tan]", "[firebrick]", "[red]", "[scarlet]", "[coral]", "[salmon]", "[pink]", "[magneta]", "[purple]", "[violet]", "[maroon]", "[crimson]"]
	temp = {}

def colors():
	return fw.colors, len(fw.colors)

def clear_temp(name_var: str):
	global fw
	if name_var in fw.temp:
		try:
			del fw.temp[name_var]
			return True, "ok"
		except:
			return False, "deletion-error"
	else:
		return False, "missing-variable"

def info():
	print(str(__namelib__) + " (v" + str(__version__) + ")\n" + ("-" * (24 + len(__company__) + len(__author__))) + "\nCompany is " + str(__company__) + " @ Author is " + str(__author__))

def is_color(color: str):
	testing = {"presence-of-brackets": None, "color-type": None}
	if ("[" in color) and ("]" in color):
		testing["presence-of-brackets"] = True
	else:
		testing["presence-of-brackets"] = False
	if testing["presence-of-brackets"] == True:
		ctt = re.match(r'#[0-9A-Fa-f]{6}', str(color[1:-1]))
	else:
		ctt = re.match(r'#[0-9A-Fa-f]{6}', str(color))
	if ctt == None:
		if color in fw.colors:
			testing["color-type"] = "color"
		else:
			testing["color-type"] = "str"
	else:
		testing["color-type"] = "color-code"
	return testing["presence-of-brackets"], testing["color-type"]

def add_color(color: str):
	global fw
	if not(color in fw.colors) and (is_color(color)[0] == True):
		fw.colors.append(color)

def add_colors(colors: list):
	global fw
	wag = 0
	while wag != len(colors):
		add_color(colors[wag])
		wag += 1

def save_colors(filename: str):
	global fw
	try:
		with open(filename, "w") as file:
			json.dump({"colors": fw.colors}, file)
		return True
	except:
		return False

def load_colors(filename: str):
	global fw
	if (os.path.isabs(filename)) or (filename in os.listdir()):
		if os.path.isfile(filename):
			if os.path.getsize(filename) != 0:
				try:
					with open(filename) as file:
						fdata = json.load(file)
					try:
						cdata = fdata["colors"]
					except:
						return False, "absent-colors-list"
					if len(cdata) != 0:
						wag = 0
						while wag != len(cdata):
							add_color(cdata[wag])
							wag += 1
						return True, "ok"
					else:
						return False, "null-color-list"
				except:
					return False, "failed-open"
			else:
				return False, "null-file"
		else:
			return False, "not-file"
	else:
		return False, "wrong-path"

def random_color():
	return fw.colors[random.randint(0, len(fw.colors))]

def random_colors(count: int):
	global fw
	if count > len(fw.colors):
		count = len(fw.colors)
	fw.temp["colors-added"] = []
	fw.temp["colors-done"] = []
	wag = 0
	while wag != count:
		color = str(random_color())
		if not(color in fw.temp["colors-added"]):
			fw.temp["colors-added"].append(color)
			fw.temp["colors-done"].append(color)
			wag += 1
	done = fw.temp["colors-done"]
	clear_temp("colors-done")
	clear_temp("colors-added")
	return done

def del_color_in_str(text: str):
	return (re.sub(r"(?<=\[).*?(?=\])", "", text)).replace("[", "").replace("]", "")

def tstlib():
	global fw
	testing_done = {"colors": 1, "is_color": 0, "add_color": 0, "add_colors": 0, "save_colors": 0, "load_colors": 0, "random_color": 1, "random_colors": 1}
	# 1 (max is 1)
	try:
		colors_list, colors_count = colors()
	except:
		testing_done["colors"] -= 1
	del colors_list, colors_count

	# 2 (max is 5)
	test_iscolor1 = is_color("white")
	test_iscolor2 = is_color("[]")
	test_iscolor3 = is_color("[white]")
	test_iscolor4 = is_color("#FFFFFF")
	test_iscolor5 = is_color("[#FFFFFF]")
	if (test_iscolor1[0] == False) and (test_iscolor1[1] == "str"):
		testing_done["is_color"] += 1
	if (test_iscolor2[0] == True) and (test_iscolor2[1] == "str"):
		testing_done["is_color"] += 1
	if (test_iscolor3[0] == True) and (test_iscolor3[1] == "color"):
		testing_done["is_color"] += 1
	if (test_iscolor4[0] == False) and (test_iscolor4[1] == "color-code"):
		testing_done["is_color"] += 1
	if (test_iscolor5[0] == True) and (test_iscolor5[1] == "color-code"):
		testing_done["is_color"] += 1
	del test_iscolor1, test_iscolor2, test_iscolor3, test_iscolor4, test_iscolor5

	# 3 (max is 1)
	add_color("[test]")
	if "[test]" in fw.colors:
		testing_done["add_color"] += 1
	fw.colors.remove("[test]")

	# 4 (max is 1)
	add_colors(["[test]", "[white]"])
	if "[test]" in fw.colors:
		testing_done["add_colors"] += 1
	fw.colors.remove("[test]")

	# 5 (max 2)
	if save_colors("test.cfg") == True:
		testing_done["save_colors"] += 1
	if "test.cfg" in os.listdir():
		testing_done["save_colors"] += 1

	# 6 (max 1)
	if load_colors("test.cfg")[0] == True:
		testing_done["load_colors"] += 1
	os.remove("test.cfg")

	# 7 (max 1)
	try:
		color_rand = random_color()
		del color_rand
	except:
		testing_done["random_color"] -= 1

	# 8 (max 1)
	try:
		colors_rand = random_colors(8)
		del colors_rand
	except:
		testing_done["random_colors"] -= 1
	return testing_done["colors"], testing_done["is_color"], testing_done["add_color"], testing_done["add_colors"], testing_done["save_colors"], testing_done["load_colors"], testing_done["random_color"], testing_done["random_colors"]

def testing():
	TestResults = tstlib()
	print(f"Test Results:\n\tcolors: {TestResults[0]}/1\n\tis_color: {TestResults[1]}/5\n\tadd_color: {TestResults[2]}/1\n\tadd_colors: {TestResults[3]}/1\n\tsave_colors: {TestResults[4]}/2\n\tload_colors: {TestResults[5]}/1\n\trandom_color: {TestResults[6]}/1\n\trandom_colors: {TestResults[7]}/1\nOverall result: {sum(TestResults)}/13")