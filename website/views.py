from multiprocessing.connection import wait
from flask import Blueprint,render_template, request,flash
from flask_login import login_required,current_user

from website import util
from .Scripts.Spotify_util import get_tracks_df,get_albums_df

## LOAD ENVIRONMENT VARIABLES : 
import dotenv


#setup the blueprint
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html",user=current_user)

@views.route('/download',methods=['GET','POST'])
@login_required
def download():
    if request.method =='POST':
        # get the user choices
        # 1. spotify download choices
        tracks_spotify = request.form.get('tracks_switch_spotify')
        albums_spotify = request.form.get('albums_switch_spotify')
        playlists_spotify = request.form.get('playlists_switch_spotify')

        # 2. deezer download choices
        tracks_deezer = request.form.get('tracks_switch_deezer')
        albums_deezer = request.form.get('albums_switch_deezer')
        playlists_deezer = request.form.get('playlists_switch_deezer')

        #all = list(request.form.values)
        if not(tracks_spotify=='on' or albums_spotify=='on' or playlists_spotify=='on') and not (tracks_deezer=='on' or albums_deezer=='on' or playlists_deezer=='on') :
            flash('You must Choose at least on field',category='error')
        else:
            print(f'track : {tracks_spotify}alums :{albums_spotify} playlist : {playlists_spotify}')
            dotenv.load_dotenv(dotenv.find_dotenv('.env'))
            #at least tracks,albums or playlists are 'on'
            if playlists_spotify =='on':
                #need to ask for the playlists to keep then dl
                flash('Playlists',category='succes')
                pass
            if tracks_spotify=='on':
                df_track = get_tracks_df()
                util.track_to_db(df_track,current_user)
                flash('All Favorites songs loaded Succesfully',category='succes')

            if albums_spotify=='on':
                df_albums = get_albums_df(True)
                util.album_to_db(df_albums,current_user)
                flash('All Favorites albums loaded Succesfully',category='succes')

            if tracks_deezer =='on':
                import time
                time.sleep(5)
                flash('Download from Deezer not available yet, come back soon..',category='error')
            if albums_deezer =='on':
                flash('Download from Deezer not available yet, come back soon..',category='error')
            if playlists_deezer =='on':
                flash('Download from Deezer not available yet, come back soon..',category='error')

    return render_template("download.html",user=current_user)

@views.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    return render_template("upload.html",user=current_user)



    