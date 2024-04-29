from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from flask.data_api import *

app = Flask(__name__)
CORS(app)



@app.route('/sub', methods=['POST'])
def sub():
    name = request.form.get()
    return jsonify(data)

@app.route('/data')
def get_data():
    data = {'message': 'API DATA'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)