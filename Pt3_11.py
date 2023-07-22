s = [a for a in input('Введите строку: ').replace(' ','') if a.isalpha()]
dict = {sorted(list(set(s)))[i]:1 for i in range(len(set(s))) if (s.count(sorted(list(set(s)))[i]) == 1) }
print(dict)
