for $j(1..100){$s="";$s=("fizz"x($j%3<1)."buzz"x($j%5<1));if(""eq$s){$s=$j;}
	print $s."\n"
}
