def longest_common(elso, masodik, x, y):

	if x == 0 or y == 0:
	    return 0;
	elif elso[x-1] == masodik[y-1]:
	    return 1 + longest_common(elso, masodik, x-1, y-1);
	else:
	    return max(longest_common(elso, masodik, x, y-1), longest_common(elso, masodik, x-1, y));


elso = "FGHJKAERT"
masodik= "HJKEORPD"
print "Length of LCS is ", longest_common(elso , masodik, len(elso), len(masodik))
