def d(l):
	j=b=0;m=l[j];r=[]
	for i in l:
		(m,b)=[(m,0),(i,1)][i>=m]
		if b>0:r+=[i]
	j+=1
	l[:]=r

p=[9,5,10,11,15,14,20,18,21]
print p
d(p)
print p
