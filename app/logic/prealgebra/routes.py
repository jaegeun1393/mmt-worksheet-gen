"""Route declaration."""
#system imports
from flask import *
from app import db
from .decimal_place import Decimal_Places
from .prealgebraforms import generator, example
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
    print("=", form.validate_on_submit())
    if 'response' in session:
        login = True
    
    if request.method == 'POST' and form.validate(): 
        #wkst = Wkst(form.Enump.data, form.Emin.data, form.Emax.data,
        #            form.Mnump.data, form.Mmin.data, form.Mmax.data,
        #            form.Hnump.data, form,Hmin.data, form.Hmax.data)

        givechange = True
        return redirect(
            url_for('prealgebra.prealgebra_sec1')
        )
    elif request.method == 'POST' and not form.validate(): 
        return 'ERROR'

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
    
    return render_template( #GET return
        'prealgebra/prealgebra.html', 
        data = login,
        form = form,
        seed = '1-1-1',
        descripstion = 'prealgebra/01'
    )

@prealgebra_bp.route('/example', methods=["GET", "POST"])
def hello_html():
    form = example()
    print("=", form.validate_on_submit())
    if request.method == 'POST' and form.validate_on_submit(): 
        wkst = Wkst(form.username.data)
        return 'Thank you'

    return render_template(
        'prealgebra/example.html', 
        form = form,
        descripstion = 'this is the example'
        )

#@prealgebra_bp.route('/hello', defaults={'name': 'World'})
#def hello_html(name):
#    return render_template(
#        'prealgebra/example.html', 
#        name=name,
#        descripstion = 'this is the example'
#        )

#@prealgebra_bp.route('/hello_<name>.pdf')
#def hello_pdf(name):
#    # Make a PDF straight from HTML in a string.
#    html = render_template('prealgebra/example.html', name=name)
#    return render_pdf(HTML(string=html))
