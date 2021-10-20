from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello world bigger .....</h1>'

@app.route('/weather')
def weather_info():
    return 'In pmr, it is raining'

# from flask import Flask,render_template
# app= Flask(__name__)
#@app.route('/homepage')
#def home_page():
 # return render_template('home.html')

@app.route('/market')
def market_page():
    items=[
        {'id': 1,'name':'phone','barcode':'777777773564'},
        {'id': 2, 'name': 'laptop', 'barcode': '442255345627'},
        {'id': 3, 'name': 'keyboard', 'barcode': '774545647247'}


    ]
    return render_template('market.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)





