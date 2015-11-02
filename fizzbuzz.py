print '\n'.join(['fizz'*(x%3>1)+'buzz'*(x%5>3)or str(x+1)for x in range(100)])
