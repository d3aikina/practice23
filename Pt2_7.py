s = 0
while True:
  n=int(input('Введите число: '))
  if n>=0:
    print('Число неотрицательное. Конец.')
    break
  else:
    s += n
    print(f'Сумма чисел равна {s}')
