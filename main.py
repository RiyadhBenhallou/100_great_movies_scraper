from bs4 import BeautifulSoup
import lxml
import requests

content = requests.get('https://www.empireonline.com/movies/features/best-movies-2/').text

soup = BeautifulSoup(content, 'lxml')
movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

with open('movies.txt', 'w') as file:
  for movie in movies:
    file.write(f'{movie.text}\n')