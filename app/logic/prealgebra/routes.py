"""Route declaration."""
#system imports
from flask import *
#from .prealgebraforms import DecimalPlace
from app import db
from .decimal_place import Decimal_Places
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
    if 'response' in session:
        login = True

    if request.method == 'GET':
        return render_template(
            'prealgebra/prealgebra.html', 
            data = login,
            seed = '1-1-1',
            descripstion = 'prealgebra/01'
        )
    else:
        sname = request.form['studnetName']
        tname = "aiden O."
        seed = request.form['master']
        title = request.form['pdftitle']
        desc = request.form['pdfdesc']
        master = str(Decimal_Places(seed))
    
    #custom function
        cur = db.connection.cursor()
        cur.execute("INSERT INTO mmtseed VALUES(%s, %s, %s, %s, %s)", (title, desc, sname, tname, master))
        db.connection.commit()
        cur.close()
        return render_template(
            'prealgebra/prealgebra.html', 
            seed = '1-1-1',
            descripstion = 'prealgebra/01'
        )

@prealgebra_bp.route('/editing', methods=["GET", "POST", "PUT"])
def prealgebra_edit():
    if request.method == 'GET':
        cur = db.connection.cursor()
        cur.execute("SELECT title FROM mmtseed WHERE sname LIKE 'jaegeun'")
        title = cur.fetchall()
        
        cur.execute("SELECT sname FROM mmtseed WHERE sname LIKE 'jaegeun'")
        sname = cur.fetchall()
        
        cur.execute("SELECT tname FROM mmtseed WHERE sname LIKE 'jaegeun'")
        tname = cur.fetchall()

        cur.execute("SELECT seed FROM mmtseed WHERE sname LIKE 'jaegeun'")
        seed = cur.fetchall()

        arr = [title, sname, tname, seed]
        return render_template(
            'prealgebra/editing.html', 
            nav=nav , 
            darr = arr,
            descripstion = 'prealgebraEdit'
        )
    elif request.method == 'POST':
        return render_template(
            'prealgebra/editing.html', 
            nav=nav , 
            descripstion = 'prealgebraEdit'
        )
    else:
        return render_template(
            'prealgebra/editing.html',
            nav = nav,
            descripstion = 'prealgebraEdit'
        )