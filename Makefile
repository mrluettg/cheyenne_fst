all:
	hfst-lexc chy.lexc -o chy.lexc.hfst
	hfst-twolc chy.twol -o chy.twol.hfst
	hfst-compose-intersect -1 chy.lexc.hfst -2 chy.twol.hfst -o chy.gen.hfst
	hfst-invert chy.gen.hfst > chy.mor.hfst