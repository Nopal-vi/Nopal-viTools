import json
from urllib import request

def main_i(): # URL
    try:
        Update = 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update'
        db = request.urlopen(Update)
        content = db.read()

        json_Update = json.loads(content.decode('utf-8'))
        for Update in json_Update:
            print(f"MENSAJE: {Update['title']}")
    except:
        json_error()

def json_error():
    print('MENSAJE: ERROR, NO CONECTION!')

def update_json(): # Version
    try:
        Update = 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update'
        db = request.urlopen(Update)
        content = db.read()

        json_Update = json.loads(content.decode('utf-8'))
        for Update in json_Update:
            print(f"VERSION NECESARIA: {Update['about']}")
    except:
        json_error()
