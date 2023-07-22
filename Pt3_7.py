print({x: (lambda a: True if a in 'аеёиоуыэюяaeiou' else False)(x) for x in sorted(list(set(input('Введите строку: ').lower().replace(' ','')))) if x.isalpha()})
