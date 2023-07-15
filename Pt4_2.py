s = input('Введите строку: ')
r = []
for i in range(len(s)):
  x = s[i]
  for j in range(1,min(len(s)-i, i+1)):
    if s[i-j]==s[i+j]:
      x = s[i-j] + x + s[i-j]
      r.append(x)
    else:
      break
  if i<len(s)-1:
    if s[i]==s[i+1]:
      x = s[i:i+2]
      r.append(x)
      for j in range(1,min(len(s)-i-1, i+1)):
        if s[i-j]==s[i+j+1]:
          x = s[i-j] + x + s[i+j+1]
          r.append(x)
        else:
          break
print('Все подстроки, являющиеся палиндромами:',', '.join(r))