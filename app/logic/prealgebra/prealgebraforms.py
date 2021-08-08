from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, validators
from wtforms.validators import InputRequired

#problem creation
class generator(FlaskForm):
    Enump = IntegerField('Enumprob', [validators.NumberRange(min=0, max=100)])
    Emin = IntegerField('Eminnum')
    Emax = IntegerField('Emaxnum')
    Mnump = IntegerField('Mnumprob')
    Mmin = IntegerField('Mminnum')
    Mmax = IntegerField('Mmaxnum')
    Hnump = IntegerField('Hnumprob')
    Hmin = IntegerField('Hminnum')
    Hmax = IntegerField('Hmaxnum')

#form for general pdf information
"""
class generalinfo(FlaskForm):
    suid = StringField('suid', [validators.Length(min=35, max=40)])
    tuid = StringField('tuid', [validators.Length(min=35, max=40)])
    sname = 
    title = 
    desc = 
"""
