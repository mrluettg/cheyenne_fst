all: chy.gen.hfst chy.mor.hfst 

chy.lexc.hfst: chy.lexc
	hfst-lexc $< -o $@

chy.twol.hfst: chy.twol
	hfst-twolc $< -o $@

chy.gen.hfst: chy.twol.hfst chy.lexc.hfst
	hfst-compose-intersect -1 chy.lexc.hfst -2 chy.twol.hfst -o $@ 

chy.mor.hfst: chy.gen.hfst
	hfst-invert $< -o $@

clean:
	rm *.hfst
