from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Список подключенных игроков
connected_users = []

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    if len(connected_users) < 4:
        connected_users.append(request.sid)
        emit('connected', len(connected_users))

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in connected_users:
        connected_users.remove(request.sid)
        emit('disconnected', len(connected_users))

@socketio.on('start_game')
def handle_start_game():
    # Здесь можно начать игру и обмениваться сообщениями между игроками
    pass

if __name__ == '__main__':
    socketio.run(app)
