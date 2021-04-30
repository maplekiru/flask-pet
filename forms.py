"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField 
from wtforms.validators import InputRequired, Optional, URL

class NewPetForm(FlaskForm):
    """Form for adding new pet"""
    name = StringField("Name",
                       validators=[InputRequired()])
    
    species = SelectField("Species",
                choices=[('dog', 'Dog'),
                         ('cat', 'Cat'),
                         ('porcupine', 'Porcupine')],
                         validators=[InputRequired()])
    
    photo_url = StringField("Photo url",
                       validators=[Optional(), URL()])
    
    age = SelectField('Age',
                choices=[('baby', 'Baby'),
                         ('young', 'Young'),
                         ('adult', 'Adult'),
                         ('senior', 'Senior')],
                         validators=[InputRequired()])
    
    notes = StringField("Notes",
                       validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editting a pet"""

    photo_url = StringField("Photo url",
                       validators=[Optional(), URL()])
    
    notes = StringField("Notes",
                       validators=[Optional()])

    available = BooleanField("Available",
                       validators=[Optional()])
   