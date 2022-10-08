from ast import Str
import os
import platform
import json
import time
from urllib import request

# Windows and Linux - Nopal Clear
def clear():
    if platform.system == 'Windows':
        os.system('clear') # Otros Sistemas Operativos
    else:
        os.system('cls') # Windows

Update = 'https://my-json-server.typicode.com/Nopal-vi/Nopal-viTools/update'
Info = 'Nopal-viTools [Version0.1] - Nopal-vi Organization'

db = request.urlopen(Update)
content = db.read()

json_Update = json.loads(content.decode('utf-8'))
def HOME_HOUSE():
    clear()
    for Update in json_Update:
        print(f"MENSAJE: {Update['title']}")
    print(Info)
    print('')
    print('Nopal-viTools es una herramienta utilizando la documentacion de FFmpeg\n\
para la conversion de video en (.avi) sea disponible en Tuna-viDS')
    print('')
    print(' 1- 256x192: Resolucion de pantalla completa')
    print(' 2- 256x144: Recomendado por usuarios de Nopal-viTools')
    print('')
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
        else:
            print('Hubo un error, comando no disponible!')
            home = input('>>> ')
            if home == '1':
                os.system('ffmpeg -i vid_source.mp4 -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '2':
                os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '3':
                os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '4':
                os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
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
        else:
            print('Hubo un error, comando no disponible!')
            home = input('>>> ')
            if home == '1':
                os.system('ffmpeg -i vid_source.mp4 -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '2':
                os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '3':
                os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            if home == '4':
                os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
                print('PROCESO TERMINADO!')
                time.sleep(2)
                HOME_HOUSE()
            else:
                print('Hubo un error, comando no disponible!')
    else:
        print('Hubo un error, comando no disponible!')
    time.sleep(2)
    HOME_HOUSE()

if __name__ == '__main__':
    HOME_HOUSE()
