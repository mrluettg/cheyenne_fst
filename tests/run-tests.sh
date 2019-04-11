cat phon.tsv  | sed 's/\t\t*/\t/g' | cut -f4 | hfst-pair-test ../chy.twol.hfst
