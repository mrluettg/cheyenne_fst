import sys, re

plurals = {}

for line in sys.stdin.readlines():
	if line.count('Plural')> 0:
		row = line.split(' ')
		form = row[0]
		pl = line.split('Plural')[1]
	
		pl = pl.strip().split(' ')[0].strip(';.')
		plsuff = re.sub('^' + form, '', pl)
		if plsuff not in plurals:
			plurals[plsuff] = []

		plurals[plsuff].append(form)
#		print('%s | %s | %s' % (plsuff, form, pl))


for suff in plurals:
	for form in plurals[suff]:
		print(suff, '|', form)
