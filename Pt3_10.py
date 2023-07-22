s = [a for a in input('Введите строку: ').replace(' ','') if a.isalpha()]
dict = {sorted(list(set(s)))[i]:s.count(sorted(list(set(s)))[i]) for i in range(len(set(s)))}
print(dict)
