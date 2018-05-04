def lcs(first, second, x, y):

	if x == 0 or y == 0:
	    return 0;
	elif first[x-1] == second[y-1]:
	    return 1 + lcs(first, second, x-1, y-1);
	else:
	    return max(lcs(first, second, x, y-1), lcs(fisrt, second, x-1, y));


first = "FGHJKAERT"
second = "HJKEORPD"
print "Length of LCS is ", lcs(first , second, len(first), len(second))
