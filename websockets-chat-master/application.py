import os 
from flask import Flask, render_template, send_from_directory
from flask.ext.socketio import SocketIO, emit

application = Flask(__name__)
application.debug = True
application.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(application)

clients = []

@application.route('/')
def index():
    print('loaded index')
    return "I'm live!"
    
@application.route('/chat')
def chat():
    return render_template('app/index.html')

@application.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('templates/app', path)

@socketio.on('echo', namespace='/echo')
def echo(message):
    emit('response', {'data': 'echo: ' + message['data']})


@socketio.on('message', namespace='/echo')
def message(message):
    data = message['data']
    print('%s said %s' % (data['user'], data['text']))
    emit('response', {
         'data': {'user': data['user'], 'text': data['text']}}, broadcast=True)


@socketio.on('join', namespace='/echo')
def join(message):
    clients.append(message['data'])
    emit('joined', {'data': '%s is online' % message['data']}, broadcast=True)


@socketio.on('connect', namespace='/echo')
def connect():
    emit('connect', {'data': 'Connected', 'users': clients})


@socketio.on('disconnect', namespace='/echo')
def disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(application, host='0.0.0.0', port=int(os.environ['PORT']))
