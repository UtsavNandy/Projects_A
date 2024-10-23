from bs4 import BeautifulSoup
import requests
import spotipy

date = input("Which year do you want to travel through music ?Format YYYY-MM-DD :")

response = requests.get(f"https://www.billboard.com/charts/hot-100/"+ date)
soup = BeautifulSoup(response.text, 'html.parser')

all_songs = soup.select("li ul li h3")
songs_list =[songs.getText().strip() for songs in all_songs]
print(songs_list)

