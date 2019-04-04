import re
#makes the file of the dictionary easier for an algorithm to read. 
#Basic format is: pos word (FEATURE word)
#REPLACE FINAL e-accent WITH %{e%}
import re
#word_pos = ["na", "ni", "poss", "vai", "vii", "vta", "vti", "cj", "p", "pv", "ppl", "i""fai", "fii", "fta", "fti", "fni", "fna", "m", "mbp", "i", "theme", "voice", "sfx", "pfx"]

word_pos = {"na":"NOUN-A",
"ni":"NOUN-I",
"fna":"FINAL-NA",
"fni":"FINAL-NI", 
"vai":"VERB-AI", 
"vii":"VERB-II",
"vta":"VERB-TA", 
"vti":"VERB-AI",
"fai":"FINAL-VAI",
"fii":"FINAL-VII", 
"fta":"FINAL-VAT", 
"fti":"FINAL-VIT",  
"poss":"POSS", 
"cj":"CONJUNCT", 
"p":"PARTICLE", 
"pv":"PREVERB", 
"ppl":"PARITICIPLE", 
"i":"INITIAL",
"m":"MEDIAL", 
"mbp":"MEDIAL-BP", 
"theme":"THEME", 
"voice":"VOICE", 
"sfx":"SUFFIX", 
"pfx":"PREFIX"}

file = open("cheyenne_dict_raw.txt", 'r')
prev_word = ""
prev_pos = ""
#account for var
#account for numbers at end of word. 
def trim_word(word): 
	new_word = ""
	for char in word: 
		if char == ".": continue
		elif char == ":": continue
		elif char == "-": continue
		elif char == ",": continue
		elif char == ";": continue
		elif re.search("[0-9]", char): continue
		else: new_word += char
	new_word = new_word.lower()
	if new_word and new_word[0] == "(" and new_word[-1] == ")": 
		new_word = new_word.strip("(")
		new_word = new_word.strip(")")
	return new_word

#accounts for parenthesis in the word by duplicating with parenthesis. 
def alt_paren(print_string):
	str_lst = print_string.split("\n")
	mod_line = "\n"
	new_print_string = ""
	for line in str_lst: 
		if re.search("\(", line): 
			mod_line = line
			line = line.replace("(", "")
			line = line.replace(")", "")
		new_print_string += "\n" + line 
	new_line = "\n"
	on = True
	for char in mod_line: 
		if char == "(": on = False
		if on: new_line += char
		if char == ")": on = True
	return new_print_string + "\n" + new_line

def eao_end_multichar(print_string): 
	line_lst = (print_string.split("\n"))
	return_str = ""
	for line in line_lst:
		if not line: continue
		if line[-1] == "á":
			line = line[:-1]
			line += "%{á%}"
		if line[-1] == "é": 
			line = line[:-1]
			line += "%{é%}"
		if line[-1] == "ó": 
			line = line[:-1]
			line += "%{ó%}"
		return_str += line + "\n"
	return return_str


prev_word = ""
pos_word = ""	
for line in file: 
	print_string = ""
	line_lst = line.split()
	if not line_lst: continue
	if re.search("[0-9]", line_lst[0]):
		if len(line_lst) > 2 and trim_word(line_lst[2]) in word_pos: 
			print_string += word_pos[trim_word(line_lst[2])]+ " " + prev_word
	if trim_word(line_lst[1]) in word_pos: 
		prev_word = trim_word(line_lst[0])
		prev_pos = trim_word(line_lst[1])
		print_string += word_pos[prev_pos]+ " " + prev_word
	for i in range(len(line_lst)): 
		if line_lst[i] == "var:": 
			print_string += "\n" + word_pos[prev_pos] + " " + trim_word(line_lst[i + 1])
		if len(line_lst) < 1: continue
		if trim_word(line_lst[i]) in word_pos and len(trim_word(line_lst[i])) < len(line_lst[i]):
			if i > 2 and i + 1 < len(line_lst):
				print_string += "\n" + word_pos[trim_word(line_lst[i])] + " " +  trim_word(line_lst[i+1])
		if trim_word(line_lst[i]) == "plural" and print_string != "": 
			print_string += "\nPLURAL " + trim_word(line_lst[i + 1])
		if trim_word(line_lst[i]) == "singular" and print_string != "": 
			print_string += "\nSINGULAR " + trim_word(line_lst[i + 1])
		if trim_word(line_lst[i]) == "plural" and print_string != "": 
			print_string += "\nOBVIATATIVE " + trim_word(line_lst[i + 1])
	if print_string: 
		print_string = print_string.strip(" ")
		print_string = print_string.replace("(n)", "%{n%}")
		if re.search("\(", print_string) and re.search("\)", print_string): 
			print_string = alt_paren(print_string)
		print_string = print_string.replace("ā", "a")
		print_string = print_string.replace("ē", "e")
		print_string = print_string.replace("ō", "o")
		print_string = print_string.replace("tse", "%{t%}e") #part of the phonetics. {te} never appears. 
		if re.search("FINAL-V", print_string) or re.search("VERB-", print_string): 
			print_string = eao_end_multichar(print_string)
		print(print_string)
			
		