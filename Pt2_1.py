import random
colors = {
    'оранжевый':'Апельсин',
    'голубой':'Небо',
    'белый':'Снег',
    'зеленый':'ТПУ',
    'красный':'Мухомор',
}
my_color = random.choice(list(colors.keys()))
while True:
  print('Доступны 5 цветов :', ' '.join(colors.keys()))
  user_color = input('Напишите ваш цвет: ')
  if user_color == my_color:
    print('Отлично!')
    break
  else:
    print(colors[my_color])
