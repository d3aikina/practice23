s = input('Введите строку: ')
r = ''
for i in s:
  if i.isalpha():
    if i == i.lower():
      r+=i.upper()
    else:
      r+=i.lower()
  else:
    r+=i
print(r)