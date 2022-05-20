import pandas as pd 
from . import db
from .models import Track



def track_to_db(df,current_user):
    print('=========================0000pute')
    if len(df) > 0:
        for index,track in df.iterrows():
            print(index)
            print(track['Tracks'])
            print(track['Artists'])
            print(track['Albums'])
            print(track['trackid'])
            print(current_user.id)
            new_track = Track(user_id=int(current_user.id),trackName=track['Tracks'],artistName=track['Artists'],albumName=track['Albums'],spotifyID=track['trackid'])
            db.session.add(new_track)
            db.session.commit()
    return True
