print([x for x in map(int, input('Введите числа через пробел: ').split()) if len([y for y in range(2,int(x**0.5+1)) if x%y==0])!=0])
