a = float(input('Введите первое число: '))
if a>int(a):
  a+=1
a = int(a)
b = int(float(input('Введите второе число: ')))+1
print(sum([x for x in range(a,b)]))
