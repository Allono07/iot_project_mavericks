from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)


def get_temperature():
    return round(26.0 + (random.randint(0, 300) / 100.0), 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temperature')
def temperature():
    temp = get_temperature()
    return jsonify({'temperature': temp, 'unit': '°C'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
