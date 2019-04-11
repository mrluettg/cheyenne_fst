for i in `cat phon.tsv  | sed 's/\t\t*/\t/g' | cut -f4 | sed 's/ /_/g'`; do 
	x=`echo $i | tr '_' ' '`;
	res=`echo $x | hfst-pair-test ../chy.twol.hfst`;
	echo $res": "$x
done
