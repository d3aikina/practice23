import itertools
l = [1,2,'a'] # здесь задается список
permutations = list(itertools.permutations(l))
for i in permutations: print(i)