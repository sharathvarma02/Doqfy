from flask import Flask, render_template, jsonify
import redis
import json

app = Flask(__name__)

# Redis setup
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/')
def index():
    data = r.get('nifty50')
    if data:
        data = json.loads(data)
    else:
        data = {}
    return render_template('index.html', data=data)

@app.route('/api/nifty50')
def api_nifty50():
    data = r.get('nifty50')
    if data:
        data = json.loads(data)
    else:
        data = {}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
