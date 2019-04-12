import re
file = open("plurals", 'r')
def get_abstract(plural):
	if plural[-4:] == "ȯtse": return plural[:-4] 
	elif plural[-5:] == "ėstse": return plural[:-5] 
	elif plural[-3:] == "o'o": return plural[:-3] 
	elif plural[-1:] == "o": return plural[:-1] 
	elif plural[-1:] == "e": return plural[:-1] 
	else: return "UNKNOWN"
def get_pos(plural):
	if plural[-4:] == "ȯtse": return "NI-PL-OT"
	elif plural[-5:] == "ėstse": return "NI-PL-ET"
	elif plural[-1:] == "o": return "NA-PL-O"
	elif plural[-1:] == "e": return "NA-PL-E"
	else: return "UNKNOWN"
for line in file: 
	line_lst = line.split()
	singular = line_lst[2]
	plural = line_lst[0]
	if singular == "ni." or singular == "na.": continue #common error. 
	#clean
	singular = singular.lower()
	plural = plural.lower()
	plural = re.sub("ma-", "%{v%}", plural)
	plural = re.sub("mȧ-", "%{v%}", plural) #weird phonetic thing. Some can't stand on their own and take weird possesives. 
	plural = re.sub("-", "", plural)
	plural = re.sub("1", "", plural)
	plural = re.sub("2", "", plural)
	plural = re.sub("\.", "", plural)
	plural = re.sub("ā", "a", plural)
	plural = re.sub("ē", "e", plural)
	plural = re.sub("ō", "o", plural)
	singular = re.sub("ma-", "", singular)
	singular = re.sub("mȧ-", "", singular)
	singular = re.sub("-", "", singular)
	singular = re.sub("1", "", singular)
	singular = re.sub("2", "", singular)
	singular = re.sub("\.", "", singular)
	singular = re.sub("ā", "a", singular)
	singular = re.sub("ē", "e", singular)
	singular = re.sub("ō", "o", singular)
	abstract = ""
	pos = ""
	if plural == "o'o": #for some reason many plural are listed as o'o
		abstract = singular 
		pos = "NA-PL-O"
	else: 
		abstract = get_abstract(plural)
		pos = get_pos(plural)
	#print("abstract: " + abstract + " pos: " + pos)
	if abstract == "UNKNOWN" or pos == "UNKNOWN" or abstract == "" or pos == "": continue
	e_cons = ["v", "p", "x", "k"]
	if abstract[-1:] in e_cons or (abstract[-1:] == "m" and singular[-2:-1] == "m"):
		abstract += "%{e%}"
	if abstract[-1:] == "t": 
		abstract += "%{s%}%{e%}"
	if singular[-2:] == "\'o": 
		abstract += "%{o%}"
	print(singular + ":" + abstract + " " + pos + " ;")
	
 
	
	
	
