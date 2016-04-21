z="".join([c for c in input()if c.isalnum()or c.isspace()or c=="_"]).split()
r=[];f=set([x[0].lower()for x in z])
for t in z:
	if t[0].lower()in f:
		r+=[t]
		f.remove(t[0].lower())
print(" ".join(r))
