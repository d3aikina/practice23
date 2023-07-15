f = open('books.csv', 'a')
n = int(input('Сколько записей Вы хотите добавить? '))
for i in range(n):
  entry = '\n'+input(f'Введите название {i+1} книги: ')+','+input(f'Введите автора {i+1} книги: ')+','+input(f'Введите год выпуска {i+1} книги: ')
  f.write(entry)
f.close()
f = open('books.csv')
author = input('Введите автора: ')
flag = True
for line in f.readlines():
  if author in line:
    line = line.split(',')
    print(line[0]+', '+line[2])
    flag = False
if flag:
  print('Книги этого автора не найдены')
f.close()