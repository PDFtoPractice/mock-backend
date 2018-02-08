from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as f:
    json_data = f.read()

data = json.loads(json_data)

@app.route('/api/', methods=['GET'])
def get_operation():
    drug = request.args.to_dict()['drug']
    operation = request.args.to_dict()['operation']
    for entry in data:
        if entry['Drug'] == drug:
            return json.dumps({'drug': drug, 'operation': operation, 'advice': entry['Advice']})

if __name__ == '__main__':
    app.run()
