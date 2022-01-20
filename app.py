from turtledemo.penrose import f

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/')
def about():
    dic = [
        {'id': 1, 'name': 'Shih Tzu', 'cat': 'Small Breed', 'ls': '12-16 years', 'origin': 'China'},
        {'id': 1, 'name': 'Golden Retriever', 'cat': 'Large Breed', 'ls': '10-12 years',
         'origin': 'Scottish Highlands'},
        {'id': 1, 'name': 'Maltese', 'cat': 'Small Breed', 'ls': '12-15 years', 'origin': 'South Central Europe'},
        {'id': 1, 'name': 'St. Bernard', 'cat': 'Large Breed', 'ls': '8-10 years', 'origin': 'Switzerland, Italy'},
        {'id': 1, 'name': 'Lhasa Apso', 'cat': 'Small Breed', 'ls': '12-14 years', 'origin': 'Tibet'}
    ]

    return render_template('num1.html', items=dic)


@app.route('/img')
def img():
    return render_template('num2.html')
