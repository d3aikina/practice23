import random
w, l, l_in_row =0, 0, 0
while l_in_row<3:
  print(f'Счет: {w}:{l}. Поражений подряд: {l_in_row}')
  choice = input('0 - орел, 1 - решка. Орел или решка? ')
  if choice in ['0','1']:
    choice = int(choice)
    randchoice = random.choice([0,1])
    if randchoice == 0:
      print('Выпал орел.')
    else:
      print('Выпала решка.')
    if choice == randchoice:
      w+=1
      l_in_row=0
    else:
      l+=1
      l_in_row+=1
  else:
    print('Это не орел и не решка.')
    break
print(f'Счет: {w}:{l}. Поражений подряд: {l_in_row}. Вы проиграли.')
