cat bible_final.txt  | hfst-proc chy.mor.hfstol  | sed 's/\$\W*\^/$\n^/g' | sort -f | uniq -c | sort -gr
