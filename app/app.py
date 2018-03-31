#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
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
    level = request.form['level']
    back = int(request.form['back'])
    result = run_search(option, back, level, )
    return json.dumps(result)

def run_search(option, back, name='level1',):
  print(back, type(back))
  mario = MarioSmart(read_file(name))
  result = ''

  if option == '0':
    result = bfs.breadth_first_search(mario, back)
  if option == '1':
    result = dfs.depth_first_search(mario)
  if option == '2':
    result = ucs.uniform_cost_search(mario, back)
  if option == '3':
    result = avara.avara_search(mario, back)
  if option == '4':
    result = a_start.a_start_search(mario, back)

  return {
    'mov': result[0].solution(),
    'depth': result[0].depth,
    'cost': result[0].path_cost,
    'node': result[1],
    'compute': "{:.10f} s".format(result[2])
  }

def read_file(name):
  with open('./static/assets/data/{}.json'.format(name)) as json_data:
    data = json.load(json_data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
