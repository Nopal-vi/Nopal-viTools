LOCAL = {
    'error_command': '',
    'int_error': 'the selected character is wrong',
    'error_ffmpeg': "'ffmpeg' no se reconoce, ve a github.com/Nopal-vi/Nopal-viTools",
    'ffmpeg': 'ffmpeg',
    'mp4': '.mp4',
    'avi': '.avi',
    'mov': '.mov',
    'wmv': '.wmv'
}

PROGRESS = 'nopal_vi'

xvids_MP4 = ' -i {}%s -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['mp4'])
xvids_AVI = ' -i {}%s -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['avi'])
xvids_MOV = ' -i {}%s -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['mov'])
xvids_WMV = ' -i {}%s -f avi -r 10 -s 256x192 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['wmv'])

xvidsi_MP4 = ' -i {}%s -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['mp4'])
xvidsi_AVI = ' -i {}%s -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['avi'])
xvidsi_MOV = ' -i {}%s -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['mov'])
xvidsi_MWV = ' -i {}%s -f avi -r 10 -s 256x144 -b 192k -bt 64k \
	-vcodec mpeg4 -deinterlace \
	-acodec libmp3lame -ar 32000 -ab 96k -ac 2'.format(PROGRESS) % (LOCAL['wmv'])

OUPUT_AVI = 'nopal_ouput.avi'


from dataclasses import dataclass
@dataclass
class EN:
    NOPAL_VI = 'Nopal-viTools is a tool using the FFmpeg documentation\n\
for the conversion of video in (.avi) is available in Tuna-viDS'
    xvids = '1- 256x192: Full screen resolution'
    xvidsi = '2- 256x144: Recommended by users of Nopal-viTools'
    RESOLUTION_IN_xvids = '''Your filename should be in (nopal_vi)
select the input format format you are using:

1: MP4 2: AVI 3: MOV 4: WMV'''
    COMPLETE = 'thanks for using Nopal-viTools'

@dataclass
class ES:
    NOPAL_VI = 'Nopal-viTools es una herramienta utilizando la documentacion de FFmpeg\n\
para la conversion de video en (.avi) sea disponible en Tuna-viDS'
    xvids = '1- 256x192: Resolucion de pantalla completa'
    xvidsi = '2- 256x144: Recomendado por usuarios de Nopal-viTools'
    RESOLUTION_IN_xvids = '''Su nombre de archivo debe estar en (nopal_vi)
selecciona el formato de formato de entrada que estas utilizando:

1: MP4  2: AVI  3: MOV  4: WMV'''
    COMPLETE = 'gracias por usar Nopal-viTools'
