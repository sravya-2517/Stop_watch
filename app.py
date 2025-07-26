from flask import Flask, jsonify, request
import time

app = Flask(__name__)

# Stopwatch state
stopwatch = {
    'start_time': None,
    'elapsed_time': 0,
    'running': False
}

@app.route('/start', methods=['POST'])
def start():
    if not stopwatch['running']:
        stopwatch['start_time'] = time.time() - stopwatch['elapsed_time']
        stopwatch['running'] = True
    return jsonify({'message': 'Stopwatch started'})

@app.route('/stop', methods=['POST'])
def stop():
    if stopwatch['running']:
        stopwatch['elapsed_time'] = time.time() - stopwatch['start_time']
        stopwatch['running'] = False
    return jsonify({'message': 'Stopwatch stopped'})

@app.route('/reset', methods=['POST'])
def reset():
    stopwatch['start_time'] = None
    stopwatch['elapsed_time'] = 0
    stopwatch['running'] = False
    return jsonify({'message': 'Stopwatch reset'})

@app.route('/time', methods=['GET'])
def get_time():
    if stopwatch['running']:
        elapsed = time.time() - stopwatch['start_time']
    else:
        elapsed = stopwatch['elapsed_time']
    return jsonify({'elapsed_time': round(elapsed, 2)})

if __name__ == '__main__':
    app.run(debug=True)

