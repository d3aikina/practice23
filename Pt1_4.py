while True:
  num = float(input('Введите число в диапазоне от 10 до 20: '))
  if num < 10: print('Число меньше требуемого диапазона')
  elif num > 20: print('Число больше требуемого диапазона')
  else:
    print('Спасибо')
    break