from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

with open('data.json', 'r') as f:
    json_data = f.read()

data = json.loads(json_data)

@app.route('/api/operation', methods=['GET'])
def get_operation():
    drug = request.args.to_dict()['value1']
    operation = request.args.to_dict()['value2']
    for entry in data:
        if entry['Drug'] == drug:
            return json.dumps({'type': 'Drug-Operation', 'type1': 'Current Medication', 'type2': 'Operation', 'value1': drug, 'value2': operation, 'advice': entry['Advice'], 'source': 'Drug operation interaction research'})

@app.route('/api/condition', methods=['GET'])
def get_condition():
    drug = request.args.to_dict()['value1']
    condition = request.args.to_dict()['value2']
    return json.dumps({'type': 'Drug-Condition', 'type1': 'Current Medication', 'type2': 'Condition', 'value1': drug, 'value2': condition, 'advice': 'TODO', 'source': 'Drug condition interaction research'})

@app.route('/api/interaction', methods=['GET'])
def get_interaction():
    drug1 = request.args.to_dict()['value1']
    drug2 = request.args.to_dict()['value2']
    return json.dumps({'type': 'Drug Interaction', 'type1': 'Current Medication', 'type2': 'New Medication', 'value1': drug1, 'value2': drug2, 'advice': 'TODO', 'source': 'Drug interaction research'})

if __name__ == '__main__':
    app.run()
