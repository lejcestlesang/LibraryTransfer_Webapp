# create models for users 
# and for songs / playlists/albums

# from init import db
from . import db
from flask_login import UserMixin
from sqlalchemy import Identity

# create object to be used in db
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(150))

    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
#    tracks = db.relationship('Track')
#    albums = db.relationship('Album')
#    playlist = db.relationship('Playlist')


class Track(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    trackName = db.Column(db.String(100))
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.Integer)
    deezerID = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    playlist_id = db.Column(db.Integer,db.ForeignKey('playlist.id'))


class Album(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.Integer)
    deezerID = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


class Playlist(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    playlistName = db.Column(db.String(100))
    spotifyID = db.Column(db.Integer)
    deezerID = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    tracks = db.relationship('Track')
