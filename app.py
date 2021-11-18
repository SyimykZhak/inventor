from flask import Flask, request
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def example():
    f = open('goods.txt', 'r+', encoding='utf-8')
    txt = f.readlines()
    return render_template('index.html', goods=txt)

@app.route('/add/', methods = ["POST"])
def add():
    good = request.form["good"]
    f = open('goods.txt', 'a+', encoding='utf-8')
    f.write(good + "\n")
    f.close()
    return """
    <h1>Успешно добавлен</h1>
    <a href ='/'>Domoi</a>

    """

@app.route('/<test>/')
def mainpage(test):
    test = test.upper()
    return render_template('index.html', my_var=test)

def create_app():
   return app