"""Route declaration."""
#system imports
from flask import Blueprint, render_template
from .prealgebraforms import DecimalPlace
prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')

#nav List
nav = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Prealgebra', 'url': '/prealgebra'},
    {'name': 'Algebra', 'url': '/algebra'},
    {'name': 'Contact', 'url': '/contact'}
    #{'name': 'Signup', 'url': '/signup'}
]



@prealgebra_bp.route('/')
def prealgebra_main():
    return render_template(
        'prealgebra/prealgebra.html', 
        nav=nav , 
        descripstion = 'prealgebra/01'
        )

@prealgebra_bp.route('/1-1-1', methods=["GET", "POST"])
def prealgebra_sec1():
    
    return render_template(
        'prealgebra/prealgebra.html', 
        seed = '1-1-1',
        nav=nav , 
        descripstion = 'prealgebra/01'
    )

@prealgebra_bp.route('/01_decimal_place')
def decimal_place():

    return render_template('prealgebra/01_decimal_place.html')

@prealgebra_bp.route('/02_decimal_place')
def reading_writing():

    return render_template('prealgebra/02_naming.html')