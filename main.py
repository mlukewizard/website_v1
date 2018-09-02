from flask import Flask, render_template, flash, redirect

from forms.login_form import LoginForm
from forms.segmentation_form import SegmentationForm
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
        this_user = User(email_address=form.email_address, first_name = form.first_name,
                         last_name=form.last_name, password=form.password)
        add_user(this_user)
        return redirect('/')
    return render_template('register.html', form=form)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luke'}
    posts = [
        {
            'author': {'username': 'Sarah'},
            'body': 'I love cats!!'
        },
        {
            'author': {'username': 'Noreen'},
            'body': 'I love cats more!'
        }
    ]
    #return render_template('landing_page_template/landing_page.html', title='Home', user=user, posts=posts)
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    return render_template('login.html', title='Sign In', form=form)

@app.route('/segmentation', methods=['GET', 'POST'])
def segmentation():
    form = SegmentationForm()
    return render_template('segmentation.html', title='Sign In', form=form)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port='80')
    app.run()
    app.debug = True