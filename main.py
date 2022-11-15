from assets import data
from assets import locate
import os

about = {'title': 'Nopal-viTools [Version 0.6] - Nopal-vi Organization'}

def client_start():
    print('%s' % (about['title']))
    lenguage = str(input('''select a language:
ES: Spanish
EN: English
-> '''))
    if lenguage == 'ES':
        def ES():
            paper()
            data.client_message()
            print('%s' % (about['title']),'\n')
            print(locate.ES.NOPAL_VI,'\n','\n',
            locate.ES.xvids,'\n',
            locate.ES.xvidsi, '\n')
            xvid = str(input('-> '))

            if xvid == '1':
                print('\n',
                locate.ES.RESOLUTION_IN_xvids, '\n')
                format = str(input('-> '))

                if format == 0:
                    pass
                elif format == '1':
                    def xvids_1():
                        try:
                            os.system(f'%s{locate.xvids_MP4} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                            print(locate.ES.COMPLETE)
                            print(os.system('pause >nul'), ES())
                        except:
                            print("'ffmpeg' no se reconoce, ve a github.com/Nopal-vi/Nopal-viTools")
                            print(os.system('pause >nul'), ES())
                    xvids_1()
                elif format == '2':
                    try:
                        os.system(f'%s{locate.xvids_AVI} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                elif format == '3':
                    try:
                        os.system(f'%s{locate.xvids_MOV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                elif format == '4':
                    try:
                        os.system(f'%s{locate.xvids_WMV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                else:
                    print('%s' % (locate.LOCAL['int_error']))
            elif xvid == '2':
                print('\n',
                locate.ES.RESOLUTION_IN_xvids, '\n')
                format = str(input('-> '))

                if format == 0:
                    pass
                elif format == '1':
                    try:
                        os.system(f'%s{locate.xvidsi_MP4} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                elif format == '2':
                    try:
                        os.system(f'%s{locate.xvidsi_AVI} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                elif format == '3':
                    try:
                        os.system(f'%s{locate.xvidsi_MOV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                elif format == '4':
                    try:
                        os.system(f'%s{locate.xvidsi_WMV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.ES.COMPLETE)
                        print(os.system('pause >nul'), ES())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                        print(os.system('pause >nul'), ES())
                else:
                    print('%s' % (locate.LOCAL['int_error']))
            else:
                print('%s' % (locate.LOCAL['int_error']))
                print(os.system('pause >nul'), ES())
        ES()

    elif lenguage == 'EN':
        def EN():
            paper()
            data.client_message()
            print('%s' % (about['title']),'\n')
            print(locate.EN.NOPAL_VI,'\n','\n',
            locate.EN.xvids,'\n',
            locate.EN.xvidsi, '\n')
            xvid = str(input('-> '))

            if xvid == '1':
                print('\n',
                locate.EN.RESOLUTION_IN_xvids, '\n')
                format = str(input('-> '))

                if format == '1':
                    try:
                        os.system(f'%s{locate.xvids_MP4} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '2':
                    try:
                        os.system(f'%s{locate.xvids_AVI} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '3':
                    try:
                        os.system(f'%s{locate.xvids_MOV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '4':
                    try:
                        os.system(f'%s{locate.xvids_WMV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                else:
                    print('%s' % (locate.LOCAL['int_error']))
            elif xvid == '2':
                print('\n',
                locate.EN.RESOLUTION_IN_xvids, '\n')
                format = str(input('-> '))

                if format == '1':
                    try:
                        os.system(f'%s{locate.xvidsi_MP4} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '2':
                    try:
                        os.system(f'%s{locate.xvidsi_AVI} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '3':
                    try:
                        os.system(f'%s{locate.xvidsi_MOV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                elif format == '4':
                    try:
                        os.system(f'%s{locate.xvidsi_WMV} {locate.OUPUT_AVI}' % (locate.LOCAL['ffmpeg']))
                        print(locate.EN.COMPLETE)
                        print(os.system('pause >nul'), EN())
                    except:
                        print('%s' % (locate.LOCAL['error_ffmpeg']))
                else:
                    print('%s' % (locate.LOCAL['int_error']))
            else:
                print('%s' % (locate.LOCAL['int_error']))
                print(os.system('pause >nul'), EN())
        EN()

    else:
        print('selected language error = {}, to select a language, write ES or EN'.format(lenguage))
        print(os.system('pause >nul'), client_start())
        
def paper():
    try:
        if os.system('cls') == 'Windows':
            os.system('cls')
    except:
        if os.system('clear') == 'Linux':
            os.system('clear')

if __name__ == '__main__':
    client_start()
