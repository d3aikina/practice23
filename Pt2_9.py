n = input('Введите число: ')
m = max([int(x) for x in n])
print(f'Максимальная цифра {n.index(str(m))+1}я с начала и {len(n) - n.index(str(m))}я с конца.')
