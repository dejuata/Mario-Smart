#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import Flask, render_template, request, json

app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './static/assets/data/'

ALLOWED_EXTENSIONS = ['txt']


@app.route('/')
def index():
    return render_template('index.html', map='level.json')

@app.route('/upload', methods=['POST'])
def upload():
  try:
    data = request.form['akey']
  except:
    data = 'bad'

  data = str(data)

  return data+'was_received'
  # if request.method == 'POST':
  #   file = request.files['file']
  #   if file and allowed_file(file.filename):
  #     filename = os.path.join(app.config['UPLOAD_FOLDER'], 'data2.txt')
  #     file.save(filename)
  #   return json.dumps({'status':'OK'})

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
