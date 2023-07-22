a, b, c = float(input('Введите a: ')), float(input('Введите b: ')), float(input('Введите c: '))
D = b**2 - 4*a*c
if D<0:
  print('Корней нет.')
elif D==0:
  print(f'Один корень, {-b/(2*a)}.')
else:
  print(f'Корни: {(-b+D**0.5)/(2*a)}, {(-b-D**0.5)/(2*a)}.')
