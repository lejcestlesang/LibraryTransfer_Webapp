# create models for users 
# and for songs / playlists/albums

# from init import db
from . import db
from flask_login import UserMixin
from sqlalchemy import Identity,Table,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref



# need to change : cut the user Id in playlist album and track, add a new relationship table with userID,trackID,albumID
#relationship user to track

#relationship table between songs and users
user_track = Table(
    "user_track",db.metadata,
    db.Column("user_id", Integer, db.ForeignKey("user.id")),
    db.Column("track_id", Integer, db.ForeignKey("track.id")),
)

#relationship table between albums and users
user_album = Table(
    "user_album",db.metadata,
    db.Column("user_id", Integer, db.ForeignKey("user.id")),
    db.Column("album_id", Integer, db.ForeignKey("album.id")),
)


# create user table  in a object to be used simply
class User(db.Model,UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(150))
    tracks = relationship("Track", secondary=user_track, back_populates="users")
    albums = relationship("Album", secondary=user_album, back_populates="users")

    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password

class Track(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    trackName = db.Column(db.String(100))
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.String(100))
    deezerID = db.Column(db.String(100))
    users = relationship("User", secondary=user_track, back_populates="tracks")

class Album(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.Integer)
    deezerID = db.Column(db.Integer)
    users = relationship("User", secondary=user_album, back_populates="albums")

# add a new table to track the login of the users
#_________________________________________________________________________________________________________
"""

# OLD version
# create object to be used in db
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(100),unique = True)
    password = db.Column(db.String(150))

    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password



class Track(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    trackName = db.Column(db.String(100))
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.String(100))
    deezerID = db.Column(db.String(100))
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

"""