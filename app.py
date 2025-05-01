from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import subprocess, itertools

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client['client']
col = db['applications']
next_num = itertools.count(start=99999, step=1)

@app.route('/api/add_application', methods=['POST'])
def add_application():
    data = request.get_json()

    application = {'name'   : data.get('name'), 
                   'address': data.get('address'),
                   'status' : "Recieved",
                   'app_num': next(next_num),
                   'notes'  : []}
    col.insert_one(application)
    ret = {'status':'success',
           'app_num':application['app_num'],
           'message': 'Application added successfully'}

    return jsonify(ret)


@app.route('/api/add_note', methods=['POST'])
def add_note():
    data = request.get_json()

    col.update_one({'app_num' : int(data.get('app_num'))},
                   {'$push': {'notes': data.get('note')}})

    ret = {'status':'success',
           'app_num':data.get('app_num'),
           'message': 'Note added successfully'}

    return jsonify(ret)


@app.route('/api/check_status', methods=['POST'])
def check_status():
    data = request.get_json()

    search = col.find_one({'app_num' : int(data.get('app_num'))}, {"status": 1})
    status = search['status']

    ret = {'status':'success',
           'app_num':data.get('app_num'),
           'message':f'Status is: {status}'}

    return ret


@app.route('/api/change_status', methods=['POST'])
def change_status():
    data = request.get_json()

    col.update_one({'app_num': int(data.get('app_num'))},
                   {'$set': {'status': data.get('status')}})

    ret = {'status':'success',
           'app_num':data.get('app_num'),
           'message':f"Status is: {data.get('status')}"}

    return jsonify(ret)


@app.route('/api/get_application', methods=['POST'])
def get_application():
    data = request.get_json()

    search = col.find_one({"app_num" : int(data.get('app_num'))})

    notes = '\n'.join(search['notes'])
    name = search['name']

    ret = {'status':'success',
           'app_num':data.get('app_num'),
           'message':f'Name: {name} \nNotes:\n {notes}'}

    return jsonify(ret)


@app.route('/')
def index():
    return render_template('index.html')


def start_mongo():
    try:
        result = subprocess.run(['systemctl', 'is-active', 'mongod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.stdout.decode().strip() == 'active':
            col.delete_many({})
            return
        else:
            result = subprocess.run(['sudo', 'systemctl', 'start', 'mongod'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            col.delete_many({})
            return
    except Exception as e:
        print(f"Mongo Failed to Start - Exception: {e}")

if __name__ == '__main__':
    start_mongo()
    app.run(debug=True, host="0.0.0.0")
