# Spotify2YTMusicPLaylistConverter

## Setup

### 1.Spotify Credentials
1.1. Get CLIENT_ID and CLIENT_SECRET from [SpotifyDev](https://developer.spotify.com/dashboard)
1.2. Paste those credentials into an .env-File

### 2.Setup YTM Credentials
#### Method 1: OAUTH
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ytmusicapi.

```bash
pip install ytmusicapi
```
Then run 

```bash
ytmusicapi oauth
```

Follow the instructions and this will generate an oauth.json file

#### Method 2: Browser Authentification

Open YoutubeMusic -> Dev Console -> look for authenticated POST Request(easiest way search for ```browse```)
Look into request header and fill the missing data in browser.json

## Generating YTM-Playlist
Change the ```playlist```-variable in the python-file with your playlist-id to generate your own youtube-music-playlist
 
