#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json
from game.utilities.utilities import format_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', map='level.json')

@app.route('/upload', methods=['POST'])
def upload():
  try:
    if request.method == 'POST':
      file = request.form['level']
      print(file)
      with open('./static/assets/data/load.json', 'w') as output:
        output.write(format_data(file))
      return json.dumps({'status': '200'})
  except:
    return json.dumps({'status': '500'})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
