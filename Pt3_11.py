s = [x for x in input('Введите строку: ').replace(' ','') if x.isalpha()]
dict = {sorted(list(set(s)))[i]:1 for i in range(len(set(s))) if (s.count(sorted(list(set(s)))[i]) == 1) }
print(dict)