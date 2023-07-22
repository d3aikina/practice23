x = round(float(input('Введите вещественное число: ')), 2)
s = '.' + str(x).split('.')[1]
s = s + '0' * (3 - len(s))
x = int(str(x).split('.')[0])
while x // 1000>0:
    s = ',' + '0' * (3-len(str(x%1000))) + str(x % 1000) + s
    x //= 1000
s = str(x) + s
print(s)
