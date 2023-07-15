import itertools
l = [int(x) for x in input('Введите список чисел через пробел: ').split()]
good = []
number = int(input('Введите число: '))
for i in range(1, len(l)+1):
  combinations = itertools.combinations(l, i)
  [good.append(comb) for comb in combinations if sum(comb) == number]
for i in good:
  print(i)