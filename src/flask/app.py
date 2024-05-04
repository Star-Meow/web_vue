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
            "ID": id if id else 109021071,
            "gender": gender if gender else 0,
            "old": old if old else 4,
            "trygame": trygame if trygame else 1,
            "q_ans": q_ans if q_ans == '' else [7] * 14,
            "ans": ans if ans == '' else ['None'] * 2  
        }
        inputdb(result)
        print(result)
        return jsonify(result)
    else:
        return jsonify({"error": "No data received"})


if __name__ == '__main__':
    app.run(debug=True)