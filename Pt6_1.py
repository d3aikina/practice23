import requests
from bs4 import BeautifulSoup
names = []
url = input('Введите ссылку на исполнителя на яндекс музыке: ').split('/')
id_ = url[len(url)-1]
try:
  r = requests.get(f'https://music.yandex.ru/users/yamusic-bestsongs/playlists/{id_}')
  soup = BeautifulSoup(r.text, features="html.parser")
  tracks = soup.findAll('div', class_='d-track__name')
  for i in range(10):
    print(f'{i+1}. {tracks[i].get("title")}')
except Exception:
  print('Не получилось')