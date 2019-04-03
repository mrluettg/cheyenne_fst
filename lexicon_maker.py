import re
#creates the LEXICON for a lexc file from the pos_lexc.txt
#replaces verbs ending in an accented vowel into a multi-char symbol for that vowel. 
#Turns PLURAL and OBVIATATIVE into classes in themselves. 
file = open("cheyenne_pos_lexc.txt", 'r')
current_pos = ""
continue_lex = {"NOUN-A":"NA",
"NOUN-I":"NI",
"FINAL-NA":"FNA",
"FINAL-NI":"FNI", 
"VERB-AI":"VAI", 
"VERB-II":"VII",
"VERB-TA":"VTA", 
"VERB-AI":"VTI",
"FINAL-VAI":"FAI",
"FINAL-VII":"FII", 
"FINAL-VAT":"FTA", 
"FINAL-VIT":"VIT",  
"POSS":"PS", 
"CONJUNCT":"CJ", 
"PARTICLE":"PAR", 
"PREVERB":"PV", 
"PARITICIPLE":"PPL", 
"INITIAL":"I",
"MEDIAL":"M", 
"MEDIAL-BP":"MBP", 
"THEME":"T", 
"VOICE":"V", 
"SUFFIX":"SFX", 
"PREFIX":"PFX",
"SINGULAR":"SG",
"PLURAL":"PL",
"OBVIATATIVE":"OBV"}
def surface_rep(word): 
	#word.replace("%{e%}", " ")#space should be accented e
	word = word.replace("%{n%}", "n")
	return word
for line in file:
	if len(line) < 1: continue
	line_lst = line.split()
	if len(line_lst) < 2: continue
	if line_lst[0] != current_pos:
		print("LEXICON " + line_lst[0])
		current_pos = line_lst[0]
	pos = line_lst[0]
	word = line_lst[1]
	print_string = surface_rep(word) + ":" + word + " " + continue_lex[pos] + " ;"
	print(print_string)
