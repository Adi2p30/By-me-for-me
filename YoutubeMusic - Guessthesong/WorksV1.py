from ytmusicapi import YTMusic
import random
import webbrowser

ytmusic = YTMusic()

def get_playlist_tracks(playlist_id):
    playlist = ytmusic.get_playlist(playlist_id)
    tracks = [track['videoId'] for track in playlist['tracks']]
    return tracks

def play_random_song(tracks, team1, team2):
    random_song = random.choice(tracks)
    youtube_music_url = f"https://music.youtube.com/watch?v={random_song}"
    webbrowser.open(youtube_music_url)
    player = input("Enter the name of the player who guessed the song correctly: ")
    if player:
        if player.lower() == team1.lower():
            scores[team1] += 1
        elif player.lower() == team2.lower():
            scores[team2] += 1
    print(f"\nCurrent Scores:\n{team1}: {scores[team1]}\n{team2}: {scores[team2]}\n")

#Replace YOUR_PLAYLIST_ID with your youtube music playlists ID
playlist_id = "YOUR_PLAYLIST_ID "

playlist_tracks = get_playlist_tracks(playlist_id)
team1 = input("Enter the name of Team 1: ")
team2 = input("Enter the name of Team 2: ")
scores = {team1: 0, team2: 0}

for _ in range(100):
    play_random_song(playlist_tracks, team1, team2)
    print("------------------------------")

print("Final Scores:")
print(f"{team1}: {scores[team1]}")
print(f"{team2}: {scores[team2]}")


