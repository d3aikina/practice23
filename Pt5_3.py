f = open('books.csv')
a,b = map(int,input('Введите диапазон через пробел: ').split())
flag = True
for line in f.readlines()[1:]:
  line = line.split(',')
  if (int(line[2])>=a) and (int(line[2])<=b):
    print(', '.join(line),end='')
    flag = False
f.close()
if flag:
  print('Книги в этом диапазоне не найдены.')