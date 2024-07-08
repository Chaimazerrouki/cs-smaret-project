from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    name= "world"
    if request.method == 'POST':
        name = request.form['name']
    return render_template('index.html', title='Home', name = name)