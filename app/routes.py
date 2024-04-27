from app import app

from flask import render_template, url_for

import csv
import os


basedir = os.path.join('./app/static/data')

def get_project_csv(fname):
    with open(os.path.join(basedir,fname), 'r', encoding='utf-8-sig') as cd:
        csv_data = csv.DictReader(cd)
        result = list(csv_data)
    return result


@app.route('/')
@app.route('/index')
def index():
    
    index_content_list = [x for x in os.listdir(os.path.join('./app/templates/index_section'))]
    proj_list = get_project_csv('pyport_data.csv')
    profex_list = get_project_csv('profex.csv')


    return render_template('index.html',
                           proj_list=proj_list,
                           profex_list=profex_list,
                           index_content_list=index_content_list,
                           )