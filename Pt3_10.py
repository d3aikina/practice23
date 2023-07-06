s = [x for x in input('Введите строку: ').replace(' ','') if x.isalpha()]
dict = {sorted(list(set(s)))[i]:s.count(sorted(list(set(s)))[i]) for i in range(len(set(s)))}
print(dict)