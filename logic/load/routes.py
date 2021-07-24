"""Route declaration."""
#system imports
from flask import Blueprint, render_template, request
#from .prealgebraforms import DecimalPlace
from app import db
load_dp = Blueprint('load',__name__, url_prefix='/load', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Load', 'url': '/loadwkst'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]

@load_dp.route('/')
def load_main():
    return render_template(
        'load/load.html', 
        nav=nav , 
        descripstion = 'load'
        )