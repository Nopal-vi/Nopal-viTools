import main
import time
import os

def resolution_x():
    main.clear()
    print('RESOLUCION ACEPTADA: 256x192')
    print('')
    print('El archivo debe ser renombrado como (vid_source) para hacer la conversion')
    print('')
    home = input('MARQUE "1" PARA CONTINUAR >>> ')
    if home == '1':
        main.clear()
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
            main.main_update()
        if home == '2':
            os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
        if home == '3':
            os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
        if home == '4':
            os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
    else:
        print('Hubo un error, comando no disponible!')
        time.sleep(2)
        resolution_x()

def resolution_y():
    main.clear()
    print('RESOLUCION ACEPTADA: 256x144')
    print('')
    print('El archivo debe ser renombrado como (vid_source) para hacer la conversion')
    print('')
    home = input('MARQUE "1" PARA CONTINUAR >>> ')
    if home == '1':
        main.clear()
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
            main.main_update()
        if home == '2':
            os.system('ffmpeg -i vid_source.avi -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
        if home == '3':
            os.system('ffmpeg -i vid_source.mov -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
        if home == '4':
            os.system('ffmpeg -i vid_source.wmv -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2 tuna-vids.avi')
            print('PROCESO TERMINADO!')
            time.sleep(2)
            main.main_update()
    else:
        print('Hubo un error, comando no disponible!')
        time.sleep(2)
        resolution_y()
