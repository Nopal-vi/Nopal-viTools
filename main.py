import data
import os
import progress
import time

os.system('title Nopal-viTools - Nopal-vi Organization')
information = 'Nopal-viTools [Version 0.5] - Nopal-vi Organization'

def main_update():
    clear()
    data.main_i()
    print(information)
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
        progress.resolution_x()
    if home == '2':
        progress.resolution_y()

    if home == '3':
        print('')
        data.update_json()
        print('VERSION ACTUAL: Nopal-viTools [Version 0.5]')
        print('')
        print(' 1- Volver menu principal')
        home = input('>>> ')
        if home == '1':
            main_update()
        else:
            print('Hubo un error, comando no disponible!')
    else:
        print('Hubo un error, comando no disponible!')
        time.sleep(2)
        main_update()
def clear():
    os.system('cls')

if __name__ == '__main__':
    main_update()

if __name__ == '__main__':
    home_house()
