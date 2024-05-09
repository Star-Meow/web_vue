from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from data_api import *

app = Flask(__name__)
cors = CORS(app)



@app.route('/sub')
def sub():
    name = {'name' : 'test'}
    return jsonify(name)

@app.route('/data', methods=['POST'])
def data():
    data = request.json
    if data:
        id = data.get('ID')
        gender = data.get('gender')
        old = data.get('old')
        trygame = data.get('trygame')
        q_ans = data.get('q_ans', [])
        ans = data['ans']
        print(ans)

        result = {
            "ID": id if id else 'None',
            "gender": gender if gender else 'None',
            "old": old if old else 'None',
            "trygame": trygame if trygame else 'None',
            "q_ans": q_ans if q_ans else [0] * 14,
            "ans": ans if ans else ['None'] * 2  
        }
        inputdb(result)
        print(result)
        return jsonify(result)
    else:
        return jsonify({"error": "No data received"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 ,debug=True)