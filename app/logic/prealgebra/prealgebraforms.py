from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, validators, StringField
from wtforms.validators import InputRequired

#problem creation
class generator(FlaskForm):
    Enump = IntegerField('Enump',
        [
            validators.Required(),
            validators.NumberRange(min=0, max= 100)
        ]
    )
    Emin = IntegerField('Emin',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 99)
        ]
    )
    Emax = IntegerField('Emax',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Mnump = IntegerField('Mnump',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Mmin = IntegerField('Mmin',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Mmax = IntegerField('Mmax',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Hnump = IntegerField('Hnump',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Hmin = IntegerField('Hmin',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )
    Hmax = IntegerField('Hmax',
        [
            validators.Required(),
            validators.NumberRange(min = 1, max = 100)
        ]
    )

#form for general pdf information
"""
class generalinfo(FlaskForm):
    suid = StringField('suid', [validators.Length(min=35, max=40)])
    tuid = StringField('tuid', [validators.Length(min=35, max=40)])
    sname = 
    title = 
    desc = 
"""


class example(FlaskForm):
    username = StringField('Username')
