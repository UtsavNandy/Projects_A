import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text,"html.parser")

all_movies =soup.find_all(name="h3",class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt",mode = "w",encoding='utf-8') as file:
    for movie in movies:
        file.write(f"{movie}\n")
