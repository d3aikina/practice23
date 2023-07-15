s, k = input('Введите строку: '), int(input('Введите смещение: '))
new_s = ''
for x in s:
  ordx = ord(x)
  if ordx in range(97, 123):
    ordx += k
    if ordx > 122:
      ordx -= 26
  elif ordx in range(65, 91):
    ordx += k
    if ordx > 90:
      ordx -= 26
  new_s += chr(ordx)
print(new_s)