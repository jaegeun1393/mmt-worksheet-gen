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
    
    if (login == True):

        return render_template(
            'user/userinfo.html',  
            data = login,
            descripstion = 'load worksheet'
            )
    else:
        return redirect(url_for('login.login_main'))