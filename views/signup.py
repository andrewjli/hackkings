from flask import render_template, current_app, redirect

from hackkings import app
from hackkings.constants import ROLES
from hackkings.forms import SignupForm
from hackkings.models import User
from flask_login import login_user, current_user

@app.route('/signup', methods=('GET', 'POST'))
@app.route('/signup/<role>', methods=('GET', 'POST'))
def signup(role=None):
    if current_user.is_authenticated():
        return redirect('/')
    print 'signup'
    signup_form = SignupForm()
    signup_form.role.choices = [(ROLES.DEVELOPER, 'I\'m a developer'), (ROLES.PROPOSER, 'I\'m a proposer!')]
    print dir(signup_form.role)

    if signup_form.validate_on_submit():
        User.create(signup_form.username.data, signup_form.email.data, 
                    signup_form.password.data, signup_form.role.data)
        return redirect('/login')
    if not role:
        return render_template('signup.html', signup_form = signup_form)
    role = role.lower().strip()
    if role == 'developer':
        signup_form.role.data = ROLES.DEVELOPER
        return render_template('signup.developer.html', signup_form = signup_form)
    elif role == 'proposer':
        signup_form.role.data = ROLES.PROPOSER
        return render_template('signup.proposer.html', signup_form = signup_form)
