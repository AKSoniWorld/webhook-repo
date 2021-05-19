from API import app
#from flask import Flask, render_template


@app.route('/API')
def index():
    return "Hello From kriyaniti"
   # return render_template('index.html')

