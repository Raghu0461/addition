from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add():
    data = request.get_json()
    a = data['a']
    b = data['b']
    output = a+b
    return(jsonify({"Addition is" : output}))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)