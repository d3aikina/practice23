n = input('Введите число: ')
if (sum([int(x)**len(n) for x in n]) == int(n)):
  print(f'{n} является числом Армстронга')
else:
    print(f'{n} не является числом Армстронга')