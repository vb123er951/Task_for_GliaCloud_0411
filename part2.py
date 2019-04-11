import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.ptt.cc/bbs/Food/index.html')
if r.status_code == requests.codes.ok:
	soup = BeautifulSoup(r.text, 'html.parser')
	title = soup.find_all('div', class_='title')
	author = soup.find_all('div', class_='author')
	date = soup.find_all('div', class_='date')
	board = soup.title
	print ('***The board title is:', board.text, '****')
	for i in range(len(title)):
		print ('***The Date:', date[i].text)
		print ('***The Author:', author[i].text)
		print ('***The Article Title:', title[i].text)
		writing_link = title[i].find('a').get('href')
		p = requests.get('https://www.ptt.cc' + writing_link)
		if p.status_code == requests.codes.ok:
			writing_soup = BeautifulSoup(p.text, 'html.parser')
			content = writing_soup.find('div', id='main-container')
			print (content.text)