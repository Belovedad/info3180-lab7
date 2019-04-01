from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app import app

class UploadForm(FlaskForm):
    description = TextAreaField("Description", validators=[DataRequired()])
    fileupload = FileField("image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
