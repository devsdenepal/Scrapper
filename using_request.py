
from bs4 import BeautifulSoup
import requests

source = requests.get('https://c2e.dev/html-css/html-basics/').text

soup = BeautifulSoup(source, 'lxml')

for title in soup.find_all('a',class_='td-sidebar-link'):
	headline = title.text
	print(headline)
