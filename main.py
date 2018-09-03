from flask import Flask, render_template, flash, redirect, session

from forms.login_form import LoginForm
from forms.register_form import RegisterForm

from database.database_interface import get_user_from_email, add_user, User
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)


@app.route('/api/<string:name>', methods=['GET'])
def apiHi(name):
    return name

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            flash("Passwords do not match")
            redirect('/register')
        elif '@' not in form.email_address.data or '.' not in form.email_address.data:
            flash('The email address provided was invalid')
        else:
            this_user = User(email_address=form.email_address.data, first_name = form.first_name.data,
                             last_name=form.last_name.data, password=form.password.data)
            add_user(this_user)
            flash('Account created successfully. Please log in.')
            return redirect('/')
    return render_template('register.html', form=form)

@app.route('/')
@app.route('/index')
def index():

    if not session.get('logged_in'):
        return render_template('landing_page.html', logged_in=False, intro_message="Log in for full access")
    else:
        return render_template('landing_page.html', logged_in=session['logged_in'], first_name=session['first_name'], intro_message="Hi {0}. Thanks for creating an account, keep your eyes peeled on this page for some quality content coming soon.".format(session['first_name']))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_records = get_user_from_email(form.email_address.data)
        if user_records is None:
            flash("The email address you entered does not match any account. Please sign up for an account.")
            return redirect('/login')
        elif form.password.data == user_records.password:
            session['logged_in'] = True
            session['first_name'] = user_records.first_name
            return redirect('/')
        else:
            flash("The password you've entered is incorrect")
            return redirect('/login')

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session['logged_in'] = False
    return redirect('/')


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port='80')
    app.run()
    app.debug = True