# create models for users 
# and for songs / playlists/albums

# from init import db
from . import db
from flask_login import UserMixin
from sqlalchemy import Identity,Table,Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref



#relationship table between songs and users
user_track = Table(
    "user_track",db.metadata,
    db.Column("user_id", Integer, db.ForeignKey("user.id")),
    db.Column("track_id", Integer, db.ForeignKey("track.track_id")),
)

#relationship table between albums and users
user_album = Table(
    "user_album",db.metadata,
    db.Column("user_id", Integer, db.ForeignKey("user.id")),
    db.Column("album_id", Integer, db.ForeignKey("album.album_id")),
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
    track_id = db.Column(db.Integer,primary_key=True)
    trackName = db.Column(db.String(100))
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.String(100))
    deezerID = db.Column(db.String(100))
    users = relationship("User", secondary=user_track, back_populates="tracks")

class Album(db.Model):
    album_id = db.Column(db.Integer,primary_key=True)
    artistName = db.Column(db.String(100))
    albumName = db.Column(db.String(100))
    spotifyID = db.Column(db.Integer)
    deezerID = db.Column(db.Integer)
    users = relationship("User", secondary=user_album, back_populates="albums")

#class Token(db.Model):


# add a new table to track the login of the users
# add a Playlists
