import tkinter as tk
import webbrowser
from ytmusicapi import YTMusic
import random
import os
import time


ytmusic = YTMusic()


def get_playlist_tracks(playlist_id):
    """Fetches all the tracks from a YouTube Music playlist."""
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

    player = input_entry.get()
    if player:
        if player.lower() == team1.lower():
            scores[team1] += 1
        elif player.lower() == team2.lower():
            scores[team2] += 1
    scores_label.config(text=f"{team1}: {scores[team1]}    {team2}: {scores[team2]}")
    played_songs.append(random_song)


def start_game():
    """Starts the game and plays 100 songs."""
    team1 = team1_entry.get()
    team2 = team2_entry.get()
    scores = {team1: 0, team2: 0}
    played_songs = []

    for _ in range(100):
        play_random_song(playlist_tracks, played_songs, team1, team2)
        print("------------------------------")

    scores_label.config(
        text=f"Final Scores: {team1}: {scores[team1]}    {team2}: {scores[team2]}"
    )


playlist_id = "PLhdJ9tvhgCPLdP47rqgbkBqbJ_Gaw5qZc"
playlist_tracks = get_playlist_tracks(playlist_id)

window = tk.Tk()
window.title("Guess the Song")
window.geometry("400x200")

team1_label = tk.Label(window, text="Team 1:")
team1_label.pack()
team1_entry = tk.Entry(window)
team1_entry.pack()

team2_label = tk.Label(window, text="Team 2:")
team2_label.pack()
team2_entry = tk.Entry(window)
team2_entry.pack()

input_label = tk.Label(window, text="Enter player name:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

scores_label = tk.Label(window, text="Scores: 0    0")
scores_label.pack()

start_button = tk.Button(window, text="Start Game", command=start_game)
start_button.pack()

window.mainloop()
