from flask import redirect, render_template
from flask.helpers import url_for
from flask_login import login_required, logout_user
from app.forms import LoginForm
from . import auth

@auth.route('/login', methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        
        pass
    
    return render_template(url_for('login-html', **context))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))