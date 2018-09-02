from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField

class SegmentationForm(FlaskForm):
    file = FileField('File')
    submit = SubmitField('Upload')
