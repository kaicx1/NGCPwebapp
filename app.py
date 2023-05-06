import os
import threading
from std_msgs.msg import String

#import rospy

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__,  template_folder='templates', static_folder='static')
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route("/", methods=['GET', 'POST'])
def index():
     return render_template('index.html')

@socketio.on("update")
def update(data):
    print('Current Value 1', data['HSV1'])
    print('Current Value 2', data['HSV2'])
    print('Current Value 3', data['HSV3'])
    print('Current Value 4', data['HSV4'])
    print('Current Value 5', data['HSV5'])
    print('Current Value 6', data['HSV6'])

if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0')
    