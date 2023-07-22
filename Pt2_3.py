n = input('Введите число: ')
if (sum([int(i)**len(n) for i in n]) == int(n)):
  print(f'{n} является числом Армстронга')
else:
    print(f'{n} не является числом Армстронга')
