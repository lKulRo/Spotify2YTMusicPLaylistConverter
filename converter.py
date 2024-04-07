from dotenv import load_dotenv
from requests import post,get
import os
import base64
import json
from ytmusicapi import YTMusic

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

playlist = "37i9dQZF1DX36edUJpD76c"

def get_access_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 =  str(base64.b64encode(auth_bytes), "utf-8")
    
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type" : "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def auth_header(token):
    return {"Authorization" : "Bearer " + token}

def get_playlist(token):
    url = f"https://api.spotify.com/v1/playlists/{playlist}?fields=name%2Ctracks.items%28track%28name%2C+artists%28name%29%29%29"
    headers = auth_header(token)
    
    trackList = []
    
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    items = json_result["tracks"]["items"]
    for item in items:
        artist = item["track"]["artists"][0]["name"]
        trackList.append(artist+" "+item["track"]["name"])
    playlist_name = json_result["name"]
    return [playlist_name, trackList]



yt = YTMusic('oauth.json')
playlist = get_playlist(get_access_token())
playlistId = yt.create_playlist(playlist[0], 'skrrr')
for item in playlist[1]:
    search_results = yt.search(item, "songs")
    yt.add_playlist_items(playlistId, [search_results[0]['videoId']])
    print(f"{item} added to {playlist[0]}")
