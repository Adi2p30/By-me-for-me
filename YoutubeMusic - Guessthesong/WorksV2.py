# Added Time and No Repition Functionality
import time
import webbrowser
from ytmusicapi import YTMusic
import random
import os


ytmusic = YTMusic()


def get_playlist_tracks(playlist_id):
    playlist = ytmusic.get_playlist(playlist_id)
    tracks = [track["videoId"] for track in playlist["tracks"]]
    return tracks


def play_random_song(tracks, played_songs, team1, team2):
    time.sleep(1)
    available_tracks = list(set(tracks) - set(played_songs))

    if not available_tracks:
        print("All songs have been played.")
        return
    random_song = random.choice(available_tracks)
    youtube_music_url = f"https://music.youtube.com/watch?v={random_song}"
    webbrowser.open(youtube_music_url)
    time.sleep(5)
    os.system("killall -9 'Google Chrome'")

    player = input("Enter the name of the player who guessed the song correctly: ")
    if player:
        if player.lower() == team1.lower():
            scores[team1] += 1
        elif player.lower() == team2.lower():
            scores[team2] += 1
    print(f"\nCurrent Scores:\n{team1}: {scores[team1]}\n{team2}: {scores[team2]}\n")
    played_songs.append(random_song)


# Replace YOUR_PLAYLIST_ID with your youtube music playlists ID
playlist_id = "PLhdJ9tvhgCPLdP47rqgbkBqbJ_Gaw5qZc"
playlist_tracks = get_playlist_tracks(playlist_id)

team1 = input("Enter the name of Team 1: ")
team2 = input("Enter the name of Team 2: ")
scores = {team1: 0, team2: 0}
played_songs = []

for _ in range(100):
    play_random_song(playlist_tracks, played_songs, team1, team2)
    print("------------------------------")

print("Final Scores:")
print(f"{team1}: {scores[team1]}")
print(f"{team2}: {scores[team2]}")
