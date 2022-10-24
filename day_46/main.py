from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

YOUR_CLIENT_SECRET = "e1151f01201c482eafa7500bc8ccc9c2"
YOUR_CLIENT_ID = "98dbf7ee40ee46ab89b219a391066f1f"
REDIRECT_URL = "http://mysiteviln.com/callback/"
# *********** Top 100 Billboard Web scraping ***********
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all("h3", class_="a-no-trucate")
song_list = [song.getText().strip() for song in song_names]

print(f"***** Billboard hot 100 Week of {date}*****\n")
songs = [print(_) for _ in song_list]

# ************* Spotify API *************

spotify_auth = spotipy.oauth2.SpotifyOAuth(client_id=YOUR_CLIENT_ID,
                                           client_secret=YOUR_CLIENT_SECRET,
                                           redirect_uri=REDIRECT_URL,
                                           scope="playlist-modify-private",
                                           cache_path="token.txt")

sp = spotipy.Spotify(oauth_manager=spotify_auth)

user_name = sp.current_user()["display_name"]
user_id = sp.current_user()["id"]

song_urls = []
for song in song_list:
    items = sp.search(q=f"track: {song}", type="track")["tracks"]["items"]
    if len(items) > 0:
        song_urls.append(items[0]["uri"])

playlist_id = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls)
