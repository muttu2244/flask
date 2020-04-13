from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
dropzone = Dropzone(app)
app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

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

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class InfoForm(FlaskForm):
    '''
    This general class gets a lot of information about a car insurer.
    Mainly a way to go through many of the WTForms Fields.
    '''
    name = StringField('Please enter your name',validators=[DataRequired()])
    insured  = BooleanField("Have you been Insured?")
    #car = RadioField('Please choose your car Model:', choices=[('car_one','Maruthi'),('car_two','Hyundai')])
    car_model = SelectField(u'Pick Your Car Model:',
                          choices=[('ma', 'Maruthi'), ('hu', 'Hyundai'),
                                   ('fo', 'Ford')])
    #chassiNumber = TextAreaField()
    chassiNumber = StringField('Please enter your Chassi Number',validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    # Create instance of the form.
    form = InfoForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the insurer on the form.

        session['name'] = form.name.data
        session['insured'] = form.insured.data
        session['car'] = form.car_model.data
        session['chassiNumber'] = form.chassiNumber.data

        #return redirect(url_for("results"))
        return redirect(url_for('results'))
    #return render_template('01-home.html', form=form)


    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

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

        session['file_urls'] = file_urls
        return "uploading..."

    return render_template('index.html', form=form)

'''
@app.route('/thankyou')
def thankyou():

    return render_template('01-thankyou.html')
'''

@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))

    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    session.pop('file_urls', None)

    return render_template('results.html', file_urls=file_urls)

if __name__ == '__main__':
    app.run(debug=True)