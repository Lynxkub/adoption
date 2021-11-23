from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, Email, URL


class PetForm(FlaskForm):
    """Pet form to build an add/edit pet form"""
    name = StringField('Name', validators = [InputRequired(message='Pet Must Have a Name')])
    species = SelectField('Species', choices = [('Dog','Dog'),('Cat','Cat'),('Bear', 'Bear')],validators = [InputRequired(message = 'Pet Must Have a Species')])
    photo_url=StringField('Photo url', validators = [Optional(), URL(message = 'Incorrect URL format')])
    age= SelectField('Age', choices = [(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)], validators = [InputRequired(message='Pet Age Must Be Declared')])
    notes = TextAreaField('Notes')