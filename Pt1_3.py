x = [int(input('Введите число : ')) for i in range(3)]
print('Наибольшее число: ', max(x), '\n', 'Отсортированный список: ', ' '.join(map(str, sorted(x, reverse = True))), sep = '')