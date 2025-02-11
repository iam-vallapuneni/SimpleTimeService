from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def get_time():
    return jsonify({
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "ip": socket.gethostbyname(socket.gethostname())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
