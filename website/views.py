from flask import Blueprint,render_template, request,flash
from flask_login import login_required,current_user
#import code of transfer


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

        all = list(request.form.values())
        if len(all)<1:
            flash('You must Choose at least on field',category='error')
        else:
            #at least tracks,albums or playlists are 'on'
            if playlists =='on':
                flash(f'{playlists}',category='succes')

            pass

    return render_template("transfer.html",user=current_user)



    