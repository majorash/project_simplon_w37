from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath
import zipfile
from .models import Album
from . import db
from .customvision import *
import pandas as pd
from PIL import Image, ImageFile
from resizeimage import resizeimage


ImageFile.LOAD_TRUNCATED_IMAGES = True


main = Blueprint('main', __name__)


UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/')
UPLOAD_FOLDER = UPLOADS_PATH
ALLOWED_EXTENSIONS = set(['zip'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():

    if request.method == 'POST':

        if 'file' not in request.files:

            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        album_name = request.form['album_name']
        album_name = album_name.replace(' ', '_').lower()
        PATHR = UPLOAD_FOLDER + str(current_user.id) + file.filename.rsplit('.', 1)[0].lower()
        
        try :
            os.mkdir(PATHR)

        except FileExistsError :
            pass
        
        if file.filename == '' :
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            file.save(os.path.join(PATHR, file.filename))
            zip_ref = zipfile.ZipFile(os.path.join(PATHR, file.filename), 'r')
            zip_ref.extractall(PATHR)
            zip_ref.close()     

            file_path = str(current_user.id) + file.filename.rsplit('.', 1)[0].lower() + '/' + file.filename.rsplit('.', 1)[0].lower()
            user_id = current_user.id

            new_album = Album(album_name=album_name, album_link=file_path, user_id=user_id)

            db.session.add(new_album)
            db.session.commit()

            it_path = str(PATHR + '/' + file.filename.rsplit('.', 1)[0].lower())

            images = os.listdir(os.path.join(PATHR, file.filename.rsplit('.', 1)[0].lower()))
            
            return redirect(url_for('main.upload_file', filename=filename))
        
    return render_template('createalbum.html')


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/albums', methods=['GET', 'POST'])
@login_required
def albums() :

    train = []
    albums = Album.query.filter_by(user_id=current_user.id).all()

    for i in albums :
        train.append(i.album_name)

    if request.method == 'POST':

        alb_name = request.form.get('lib')
        albums = Album.query.filter_by(album_name=alb_name).first()
        images = os.listdir(os.path.join(UPLOAD_FOLDER, albums.album_link))
        prefix = albums.album_link + '/'

        
        wagon = []

        for fichier in images :

            with open( os.path.join(UPLOAD_FOLDER, albums.album_link) + '/' + fichier, 'r+b') as f:

                with Image.open(f) as image:
                    cover = resizeimage.resize_cover(image, [224, 224])
                    cover.save(os.path.join(UPLOAD_FOLDER, albums.album_link) + '/' + fichier, image.format)
                    label = classify_photo(os.path.join(UPLOAD_FOLDER, albums.album_link) + '/' + fichier)
                    wagon.append(label)
                    length_t = len(images)


        return render_template('viewalbum.html', prefix=prefix, alb=images, label=wagon,n=length_t)

    return render_template('albums.html', alb=train)


