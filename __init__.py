from flask import Flask, render_template, flash, redirect

from forms.login_form_package.login_form import LoginForm
from config import Config
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

#bootstrap = Bootstrap(app)


@app.route('/api/<string:name>', methods=['GET'])
def apiHi(name):
    return name

@app.route('/')
@app.route('/index')
def index():
    """

    :return:
    """
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
    return render_template('landing_page_template/landing_page.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/')
    return render_template('/login_template/login.html', title='Sign In', form=form)


if __name__ == "__main__":
    app.run()
    app.debug = True
