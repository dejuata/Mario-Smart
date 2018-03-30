#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, json
from game.utilities.utilities import format_data
import json

from game.agent.mario import MarioSmart
from game.agent.node import Node
from game.algorithms.uninformed import bfs, dfs, ucs
from game.algorithms.informed import avara, a_start


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', map='level.json')

@app.route('/upload', methods=['POST'])
def upload():
  try:
    if request.method == 'POST':
      file = request.form['level']
      with open('./static/assets/data/load.json', 'w') as output:
        output.write(format_data(file))
      return json.dumps({'status': '200'})
  except:
    return json.dumps({'status': '500'})

@app.route('/game', methods=['POST'])
def game():
  if request.method == 'POST':
    option = request.form['option']
    result = run_search(option)
    return json.dumps(result)

def run_search(option, name='level1'):
  mario = MarioSmart(read_file(name))
  result = ''

  if option == '0':
    result = bfs.breadth_first_search(mario)
  if option == '1':
    result = dfs.depth_first_search(mario)
  if option == '2':
    result = ucs.uniform_cost_search(mario)
  if option == '3':
    result = avara.avara_search(mario)
  if option == '4':
    result = a_start.a_start_search(mario)
  print(result[0].solution())
  return {
    'mov': result[0].solution(),
    'depth': result[0].depth,
    'node': result[1],
    'compute': "{:.10f} s".format(result[2])
  }

def read_file(name):
  with open('./static/assets/data/{}.json'.format(name)) as json_data:
    data = json.load(json_data)
    return data

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
