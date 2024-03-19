from bs4 import BeautifulSoup
import spotipy
import requests
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "5c508e632311434e87301101c592f9ef"
CLIENT_SECRET = "ea05b7e46d28476f903b7fc7314c26ab"
REDIRECT_URI = "https://example.com/"



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Osephasvhili.dito", 
    )
)
user_id = sp.current_user()["id"]





date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, "html.parser")

titles = soup.select(selector="li h3", class_="c-title")
titels_list = [song.text.strip() for song in titles]
songs=[]

for _ in range(0, 100):
    songs.append(titels_list[_])

print(songs)

