from flask import Blueprint,render_template, request,flash
from flask_login import login_required,current_user

from website import util
from .Scripts.Spotify_util import get_tracks_df

## LOAD ENVIRONMENT VARIABLES : 
import dotenv


#setup the blueprint
views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("home.html",user=current_user)

@views.route('/transfer',methods=['GET','POST'])
@login_required
def transfer():
    if request.method =='POST':
        tracks = request.form.get('tracks_switch')
        albums = request.form.get('albums_switch')
        playlists = request.form.get('playlists_switch')
        #all = list(request.form.values)
        if not(tracks=='on' or albums=='on' or playlists=='on'):
            flash('You must Choose at least on field',category='error')
        else:
            dotenv.load_dotenv(dotenv.find_dotenv('.env'))
                        #at least tracks,albums or playlists are 'on'
            if playlists =='on':
                #need to ask for the playlists to keep then dl
                flash('',category='succes')
                pass
            if tracks=='on':
                df_track = get_tracks_df()
                util.track_to_db(df_track,current_user)
                flash('All Favorites songs loaded Succesfully',category='succes')

            if albums=='on':
                flash('',category='succes')
                pass

    return render_template("transfer.html",user=current_user)



    