import json
from urllib import request

CONECTION = {
    'url': 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update',
    'message': 'MENSAJE:',
    'error_conection': 'SIN CONEXION a INTERNET',
    'version': 'VERSION ACTUAL:',
    'update': 'VERSION NECESARIA:'
}
def client_message(): # mensaje recibido por un formato json
    try:
        url = '%s' % (CONECTION['url'])
        post = request.urlopen(url)
        content = post.read()

        decode_json = json.loads(content.decode('utf-8'))
        for url in decode_json:
            print(f"%s {url['title']}" % (CONECTION['message']))
    except:
        print(CONECTION['message'], CONECTION['error_conection'])

def client_version(): # mensaje sobre la version necesaria
    try:
        url = '%s' % (CONECTION['url'])
        post = request.urlopen(url)
        content = post.read()

        decode_json = json.loads(content.decode('utf-8'))
        for url in decode_json:
            print(f"%s {url['about']}" % (CONECTION['update']))
    except:
        print(CONECTION['message'], CONECTION['error_conection'])
