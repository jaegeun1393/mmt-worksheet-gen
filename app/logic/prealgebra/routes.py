"""Route declaration."""
#system imports
from flask import *
from app import db
from .decimal_place import Decimal_Places
from .prealgebraforms import generator
from datetime import timedelta

prealgebra_bp = Blueprint('prealgebra',__name__, url_prefix='/prealgebra', template_folder='templates',static_folder='static')

@prealgebra_bp.before_request
def makesession_permanent():
    session.permanent = True
    prealgebra_bp.permanent_session_lifetime = timedelta(minutes = 60)

@prealgebra_bp.route('/')
def prealgebra_main():
    login = False
    if 'response' in session:
        login = True
    
    return render_template(
        'prealgebra/prealgebra.html', 
        data = login,
        descripstion = 'prealgebra/01'
        )

@prealgebra_bp.route('/1-1-1', methods=["GET", "POST"])
def prealgebra_sec1():
    login = False
    form = generator(request.form)

    if 'response' in session:
        login = True

    if request.method == 'GET':
        return render_template(
            'prealgebra/prealgebra.html', 
            data = login,
            form = form,
            seed = '1-1-1',
            descripstion = 'prealgebra/01'
        )
    
    elif request.method == 'POST': 
    #    sname = request.form['studnetName']
    #    tname = "aiden O."
    #    seed = request.form['master']
    #    title = request.form['pdftitle']
    #    desc = request.form['pdfdesc']
    #    master = str(Decimal_Places(seed))
    
    #custom function
    #    cur = db.connection.cursor()
    #    cur.execute("INSERT INTO mmtseed VALUES(%s, %s, %s, %s, %s)", (title, desc, sname, tname, master))
    #    db.connection.commit()
    #    cur.close()
    
        return render_template(
            'prealgebra/prealgebra.html', 
            seed = '1-1-1',
            descripstion = 'prealgebra/01'
        )

'''
@prealgebra_bp.route('/hello', defaults={'name': 'World'})
def hello_html(name):
    return render_template(
        'prealgebra/example.html', 
        name=name,
        descripstion = 'this is the example'
        )

@prealgebra_bp.route('/hello_<name>.pdf')
def hello_pdf(name):
    # Make a PDF straight from HTML in a string.
    html = render_template('prealgebra/example.html', name=name)
    return render_pdf(HTML(string=html))
    '''