import flask
from flask import request, abort
import json
import random

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():  
    ret = {'success':True, 'mesage':'This is the home page'}
    return json.dumps(ret), 200, {'Content-Type':'application/json'}#200->success code, 404 ->could not be found, 410->used to be there, 500->server went bad, 418->teapot

@app.route('/add', methods=['GET'])
def add_numbers():
    if 'a' in request.args and 'b' in request.args:
        ans = {'answer':int(request.args['a'])+int(request.args['b'])}
        return json.dumps(ans), 200, 
        {'Content-Type':'application/json'}
    else:
        return 'nope', 400
@app.errorhandler(404)
def err_404(e):
    return "Couldn't find page", 404
app.run(host = '127.0.0.1', port = 3001)