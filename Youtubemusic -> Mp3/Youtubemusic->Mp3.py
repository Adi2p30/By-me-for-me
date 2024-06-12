import json
import pandas as pd
from pytube import YouTube
import os

df = pd.read_csv("My YouTubeMusic Playlist.csv")
# print(df)
import urllib.request
import urllib.parse
import re
import ssl
from youtubesearchpython import VideosSearch
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context
playlist = df["Track name"]
print(playlist)


def geturl(name):
    videosSearch = VideosSearch(name, limit=2)
    searchresult = videosSearch.result()
    url = "http://www.youtube.com/watch?v=" + searchresult["result"][0]["id"]
    return url


def download(url):
    yt = YouTube(url)
    stream = yt.streams.get_by_itag(251)
    destination = "/Users/adityapachpande/Downloads/Playlistmp3/"
    outfile = stream.download(output_path=destination)


for i in playlist:
    url = geturl(i)
    download(url)
