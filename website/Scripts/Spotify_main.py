import Spotify_util # other script

#useful library
import pandas as pd

## LOAD ENVIRONMENT VARIABLES : 
from dotenv import load_dotenv



def main (songs,playlists,albums):
    load_dotenv()
    if songs == 'y':
        saved_tracks = Spotify_util.get_tracks_df()
        Spotify_util.wanna_saved('Favorite_Songs',saved_tracks)
    #playlists part
    if playlists == 'y':
        df_playlists = Spotify_util.get_choose_playlists(True)
        print(df_playlists)
        Spotify_util.wanna_saved('Playlists',df_playlists)
    #Albums
    if albums == 'y':
        saved_albums = Spotify_util.get_albums_df()
        Spotify_util.wanna_saved('Favorite_Albums',saved_albums)
    

    # Artistes
if __name__ == "__main__":
    songs = input('Wanna get all favorites songs ? (y/n) :')
    playlists = input('Wanna get favorites playlists ? (y/n) :')
    albums = input('Wanna get favorites albums ? (y/n) :')
    main(songs,playlists,albums)
else: #useless
    print("main is being imported") 