all: chy.gen.hfst chy.mor.hfst chy.mor.hfstol

chy.lexc.hfst: chy.lexc
	hfst-lexc --Werror $< -o $@

chy.twol.hfst: chy.twol
	hfst-twolc $< -o $@

chy.gen.hfst: chy.twol.hfst chy.lexc.hfst
	hfst-compose-intersect -1 chy.lexc.hfst -2 chy.twol.hfst -o $@ 

chy.mor.hfst: chy.gen.hfst
	hfst-invert $< -o $@

chy.mor.hfstol: chy.mor.hfst
	hfst-fst2fst -w $< -o $@

clean:
	rm *.hfst *.hfstol
