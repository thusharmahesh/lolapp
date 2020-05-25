from flask import render_template, request
from app import app
from app.forms import LoginForm
from app.stats import WinRate

@app.route('/')
def input():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    rate = WinRate(text)
    user2 = {'rate': rate}
    return render_template('stats.html', title='Stats', user=user2)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

# @app.route('/stats')
# def stats():
#     text = my_form_post
#     rate = WinRate(text)
#     user2 = {'rate': rate}
#     return render_template('stats.html', title='Stats', user=user2)
