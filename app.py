from flask import Flask
import json

app = Flask(__name__)

with open('data.json', 'r') as f:
    json_data = f.read()

data = json.loads(json_data)

@app.route('/api/<string:drug>')
def get_operation(drug):
    for entry in data:
        print(entry)
        if entry['Drug'] == drug:
            return entry['Advice']

if __name__ == '__main__':
    app.run()
