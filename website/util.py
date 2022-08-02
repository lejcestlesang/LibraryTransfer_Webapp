import pandas as pd 
from . import db
from .models import Track,Album



def track_to_db(df,current_user):
    if len(df)==0:
        print('Error, dowloaded 0 tracks. Check track_to_db')
        return False
    if len(df) > 0:
        for index,track in df.iterrows():
            print(index)
            print(track['Tracks'])
            print(track['Artists'])
            print(track['Albums'])
            print(track['trackid'])
            print(current_user.id)
            new_track = Track(trackName=track['Tracks'],artistName=track['Artists'],albumName=track['Albums'],spotifyID=track['trackid'])
            new_track.users.append(current_user)
            db.session.add(new_track)
            db.session.commit()
    return True

def album_to_db(df,current_user):
    if len(df)==0:
        print('Error, dowloaded 0 album. Check album_to_db')
        return False
    if len(df) > 0:
        print('album_to_db started')
        for index,row in df.iterrows():
            print(index)
            print(row['Artists'])
            artist = row['Artists'].split('/')[0]
            print(row['Albums'])
            new_album = Album(artistName=artist,albumName=row['Albums'],spotifyID=row['AlbumID'])
            new_album.users.append(current_user)
            db.session.add(new_album)
            db.session.commit()
    return True

