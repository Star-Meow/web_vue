from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from data_api import *

app = Flask(__name__)
CORS(app)



@app.route('/sub', methods=['POST'])
def sub():
    data = {'name': name}
    name = request.form.get()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def data():
    data = request.json
    if data:
        id = data.get('ID')
        gender = data.get('gender')
        old = data.get('old')
        trygame = data.get('trygame')
        q_ans = data.get('q_ans', [])
        ans = data.get('ans', [])

        result = {
            "ID": id,
            "gender": gender,
            "old": old,
            "trygame": trygame,
            "q_ans": q_ans,
            "ans": ans
        }
        print(result)
        return jsonify(result)
    else:
        return jsonify({"error": "No data received"})


if __name__ == '__main__':
    app.run(debug=True)