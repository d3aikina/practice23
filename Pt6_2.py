import requests
from bs4 import BeautifulSoup

count = 1000
i = 0
games_links = []

while i < count:
	url = f'https://store.steampowered.com/search/results/?query&start={i}&count=50&dynamic_data=&force_infinite=1&filter=topsellers&ndl=1&snr=1_7_7_7000_7&infinite=1'
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.json()['results_html'], 'html.parser')
		games_links +=  [i['href'] for i in soup.findAll('a')]
	else: 
		print('Error. Response code:', r.response_code)
		exit()
	print(f'Parsed page {i//50 + 1}/{count//50 + bool(count%50)}')
	i += 50

games = {}
i = 1

for game in games_links:
	r = requests.get(game)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		name = soup.find('div', class_ = 'apphub_AppName').get_text()
		tags = [i.get_text().replace('\t', '').replace('\r', '').replace('\n', '') for i in soup.find('div', class_ = 'glance_tags popular_tags').findAll('a')]
		games[name] = tags
		print(f'{i}. Parsed {name}')
	else: 
		print('Error. Response code:', r.response_code)
		exit()
	i += 1

f = open('games.csv','w')
f.write('Game,Tags\n')
for game in games.keys():
	f.write(game+','+'; '.join(games[game])+'\n')
f.close()