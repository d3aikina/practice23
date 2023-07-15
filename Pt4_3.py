a,b = map(int,input('Введите диапазон через пробел: ').split())
a = a//2*2+1
for number in range(a,b+1,2):
  flag = True
  for i in range(3,int(number**0.5)+1):
    if number%i==0:
      flag = False
  if flag:
    print(number)