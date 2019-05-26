from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from palette import ColorFind
from uitl import *

import os

app = Flask(__name__)
dropzone = Dropzone(app)


app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods=['GET', 'POST'])
def index():
    
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )

            # append image urls
            file_urls.append(photos.url(filename))
            # 11111
            img = str('uploads/' + file.filename)
            color_thief = ColorFind(img)

            img1 = PalletteToPNG(color_thief.get_palette(quality=1))
            img2 = ColorToPNG(color_thief.get_color(quality=1))
            img1.save('uploads/' +'Palette' + file.filename)
            img2.save('uploads/' +'MainColor' + file.filename)
            # 11111
            
        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request
    return render_template('index.html')


@app.route('/results')
def results():
    
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))
        
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)
    print(file_urls[0])

    line = file_urls[0]
    index = line.find('photos/')
    output_line = line[:index+7] + 'MainColor' + line[index:]
    MainColor = output_line.replace("MainColorphotos/", "MainColor")
    print(MainColor)

    line = file_urls[0]
    index = line.find('photos/')
    output_line = line[:index + 7] + 'Palette' + line[index:]
    Palette = output_line.replace("Palettephotos/", "Palette")
    print(Palette)


    print(output_line)
    return render_template('results.html', file_urls=file_urls, main_color=MainColor, pallete=Palette)
