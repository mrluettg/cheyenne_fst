apertium-destxt | hfst-proc chy.mor.hfstol  | apertium-retxt| sed 's/\$\W*\^/$\n^/g' | sort -f | uniq -c | sort -gr
