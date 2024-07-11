import os

from app import app
from flask import render_template, url_for

from app.forms import LoginForm

from app.pyfuncs import get_project_csv



basedir = os.path.join('./app/static/data')
mdir = os.path.abspath(os.path.dirname(__name__))


@app.route('/')
@app.route('/index')
def index():
    
    index_content_list = [x for x in os.listdir(os.path.join(mdir,'app/templates/index_section'))]
    proj_list = get_project_csv(os.path.join(mdir,'app/static/data'), 'pyport_data.csv')
    profex_list = get_project_csv(os.path.join(mdir,'app/static/data'), 'profex.csv')


    return render_template('index.html',
                           proj_list=proj_list,
                           profex_list=profex_list,
                           index_content_list=index_content_list,
                           )


@app.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html',
                           form=form,
                           )