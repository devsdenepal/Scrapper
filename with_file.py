
from bs4 import BeautifulSoup
import requests

with open('404.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')
for title in soup.find_all('h1', class_='title-font'):
	
#print(match)
	headline = title.text
	print(headline)
