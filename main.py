import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

allMovies = []

movies = soup.findAll(name="h3", class_="listicleItem_listicle-item__title__BfenH")

for movie in movies:
    allMovies.append(movie.getText())

print(allMovies)

with open("mytxt.txt", "w") as file:
    for i in range(len(allMovies) - 1, -1, -1):
        file.write(allMovies[i]+"\n")

movieLink = soup.find(name="a", target="_blank")
print(movieLink)

getLink = movieLink.get("href")
print(getLink)