"""Route declaration."""
#system imports
from flask import *
from app import db
user_dp = Blueprint('user',__name__, url_prefix='/user', template_folder='templates',static_folder='static')

@user_dp.route('/')
def main_user():
    login = False
    if 'response' in session:
        login = True
        userinfo = session['response']
        role = session['role']
        role = role[slice(1, 6, 3)]
        print("=", role, "=")
    
    if (login == True):

        if(role == " ('teacher',) "): 
            print("1")
            return render_template(
                'user/Tuserinfo.html',  
                data = login,
                userinfo = userinfo,
                role = role,
                descripstion = 'load worksheet'
                )
        else:
            print("2")
            return render_template(
                'user/Suserinfo.html',  
                data = login, 
                userinfo = userinfo,
                role = role,
                descripstion = 'load worksheet'
                )

    else:
        return redirect(url_for('login.login_main'))