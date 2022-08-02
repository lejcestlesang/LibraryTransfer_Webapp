from select import select
import pandas as pd 
from . import db
from .models import Track,Album,User,user_album
from sqlalchemy import func,text

def get_or_create(session, model, defaults=None, **kwargs):
    instance = session.query(model).filter_by(**kwargs).one_or_none()
    if instance:
        return instance, False
    else:
        #kwargs |= defaults or {}
        instance = model(**kwargs)
        try:
            session.add(instance)
            session.commit()
        except Exception:  # The actual exception depends on the specific database so we catch all exceptions. This is similar to the official documentation: https://docs.sqlalchemy.org/en/latest/orm/session_transaction.html
            session.rollback()
            instance = session.query(model).filter_by(**kwargs).one()
            return instance, False
        else:
            return instance, True

def track_to_db(df,current_user,streaming_service_name='Spotify'):
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
            #new_track = Track(trackName=track['Tracks'],artistName=track['Artists'],albumName=track['Albums'],spotifyID=track['trackid'])
            if streaming_service_name == 'Spotify':
                track_instance, newone = get_or_create(db.session,Track,\
                                       trackName=track['Tracks'],artistName=track['Artists'],albumName=track['Albums'],spotifyID=track['trackid'])
            track_instance.users.append(current_user)
            #db.session.add(new_track)
            db.session.commit()
    return True

def album_to_db(df,current_user,streaming_service_name='Spotify'):
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
            #new_album = Album(artistName=artist,albumName=row['Albums'],spotifyID=row['AlbumID'])
            if streaming_service_name == 'Spotify':
                album, newone = get_or_create(db.session,Album,\
                                        artistName=artist,albumName=row['Albums'],spotifyID=row['AlbumID'])
            album.users.append(current_user)
            #db.session.add(new_album)
            db.session.commit()
    return True

def get_user_albums(current_user):
    """ get a list of all the Album of the usser

    Args:
        current_user (User instance): current User

    Returns:
        list(User): 
    """
    return current_user.albums

def get_user_tracks(current_user):
    """ get a list of all the tracks of the usser

    Args:
        current_user (User instance): current User

    Returns:
        list(Tracks): 
    """
    return current_user.tracks



def get_tracks(current_user):
    pass

def get_users():
    return db.session.query(User).all()
