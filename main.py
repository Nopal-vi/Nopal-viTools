import os
import platform
import json
from urllib import request
import time

Info = 'Nopal-viTools [Version0.2] - Nopal-vi Organization'

# Windows and Linux - Nopal Clear
def clear():
    if platform.system == 'Windows':
        os.system('clear') # Otros Sistemas Operativos
    else:
        os.system('cls') # Windows

def json_up():
    Update = 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update'
    db = request.urlopen(Update)
    content = db.read()

    json_Update = json.loads(content.decode('utf-8'))
    for Update in json_Update:
        print(f"VERSION NECESARIA: {Update['about']}")

def json_info():
    Update = 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update'
    db = request.urlopen(Update)
    content = db.read()

    json_Update = json.loads(content.decode('utf-8'))
    for Update in json_Update:
        print(f"MENSAJE: {Update['title']}")

def home_house():
    clear()
    json_info()
    print(Info)
    print('')
    print('Nopal-viTools es una herramienta utilizando la documentacion de FFmpeg\n\
para la conversion de video en (.avi) sea disponible en Tuna-viDS')
    print('')
    print(' 1- 256x192: Resolucion de pantalla completa')
    print(' 2- 256x144: Recomendado por usuarios de Nopal-viTools')
    print('')
    print(' 3- Update: Buscar actualizaciones...')
    home = input('>>> ')
    
    if home == '1':
        clear()
        print('RESOLUCION ACEPTADA: 256x192')
        print('')
        print('El archivo debe ser renombrado como (vid_source) para hacer la conversion')
        print('')
        home = input('MARQUE "1" PARA CONTINUAR >>> ')
        if home == '1':
            clear()
            print('YA ESTA CASI LISTO!')
            print('')
            print('Nos faltaria el contenedor que contiene ese archivo, para hacerlo claro el formato')
            print('')
            print(' 1- MP4  2- AVI  3- MOV  4- WMV')
            print('')
            home = input('>>> ')
            if home == '1':
                os.system('ffmpeg -i vid_source.mp4 -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '2':
                os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '3':
                os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '4':
                os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            else:
                print('Hubo un error, comando no disponible!')

    if home == '2':
        clear()
        print('RESOLUCION ACEPTADA: 256x144')
        print('')
        print('El archivo debe ser renombrado como (vid_source) para hacer la conversion')
        print('')
        home = input('MARQUE "1" PARA CONTINUAR >>> ')
        if home == '1':
            clear()
            print('YA ESTA CASI LISTO!')
            print('')
            print('Nos faltaria el contenedor que contiene ese archivo, para hacerlo claro el formato')
            print('')
            print(' 1- MP4  2- AVI  3- MOV  4- WMV')
            print('')
            home = input('>>> ')
            if home == '1':
                os.system('ffmpeg -i vid_source.mp4 -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '2':
                os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '3':
                os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            if home == '4':
                os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                home_house()
            else:
                print('Hubo un error, comando no disponible!')
    
    if home == '3':
        print('')
        json_up()
        print('VERSION ACTUAL: Nopal-viTools [Version 0.2]')
        print('')
        print(' 1- Volver menu principal')
        home = input('>>> ')
        if home == '1':
            home_house()
        else:
            print('Hubo un error, comando no disponible!')
    else:
        print('Hubo un error, comando no disponible!')
    time.sleep(2)
    home_house()



if __name__ == '__main__':
    home_house()
