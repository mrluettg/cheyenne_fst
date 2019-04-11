dmy=`date +"%Y-%m-%d"`;
total=`cat ../bible_final.txt | tr ' ' '\n' | apertium-destxt | hfst-proc ../chy.mor.hfstol | apertium-retxt | wc -l`;
known=`cat ../bible_final.txt | tr ' ' '\n' | apertium-destxt | hfst-proc ../chy.mor.hfstol | apertium-retxt | grep -v '\*' | wc -l`;
coverage=`echo "($known/$total)*100" | bc -l`
echo -e "$dmy\t$known/$total\t$coverage" >> history.log
tail -2 history.log
