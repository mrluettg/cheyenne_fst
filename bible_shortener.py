#original file deleted
eng_words = ["you", "the", "and", "who", "what", "where", "when", "why", "how", 
"this", "that", "we", "they", "them", "is", "his", "him", "of", "us"]
file = open("bible_no_punct.txt", 'r')

for line in file: 
	line_lst = line.split()
	new_line = ""
	for word in line_lst: 
		word = word.lower()
		new_line += word + " "
	print_line = True
	line_lst = new_line.split()
	for eng_word in eng_words: 
		if eng_word.lower() in line_lst: 
			print_line = False
			break
	if print_line: print(new_line)